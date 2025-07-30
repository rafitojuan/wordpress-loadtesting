import requests
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import statistics
from datetime import datetime

class LoadTester:
    def __init__(self, target_url, num_users=1000, duration=60, requests_per_user=10):
        self.target_url = target_url
        self.num_users = num_users
        self.duration = duration
        self.requests_per_user = requests_per_user
        self.results = []
        self.lock = threading.Lock()
        self.session_pool = []
        
    def create_session(self):
        session = requests.Session()
        session.headers.update({
            'User-Agent': random.choice([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            ]),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        return session
    
    def make_request(self, session, user_id):
        start_time = time.time()
        try:
            response = session.get(self.target_url, timeout=30, allow_redirects=True)
            end_time = time.time()
            response_time = end_time - start_time
            
            with self.lock:
                self.results.append({
                    'user_id': user_id,
                    'status_code': response.status_code,
                    'response_time': response_time,
                    'success': response.status_code == 200,
                    'timestamp': datetime.now(),
                    'content_length': len(response.content)
                })
                
        except requests.exceptions.RequestException as e:
            end_time = time.time()
            response_time = end_time - start_time
            
            with self.lock:
                self.results.append({
                    'user_id': user_id,
                    'status_code': 0,
                    'response_time': response_time,
                    'success': False,
                    'timestamp': datetime.now(),
                    'error': str(e),
                    'content_length': 0
                })
    
    def simulate_user(self, user_id):
        session = self.create_session()
        start_time = time.time()
        
        for request_num in range(self.requests_per_user):
            if time.time() - start_time >= self.duration:
                break
                
            self.make_request(session, user_id)
            
            think_time = random.uniform(0.1, 2.0)
            time.sleep(think_time)
        
        session.close()
    
    def run_load_test(self):
        print(f"Starting load test...")
        print(f"Target URL: {self.target_url}")
        print(f"Number of users: {self.num_users}")
        print(f"Duration: {self.duration} seconds")
        print(f"Requests per user: {self.requests_per_user}")
        print("-" * 50)
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=self.num_users) as executor:
            futures = [executor.submit(self.simulate_user, user_id) for user_id in range(self.num_users)]
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"User simulation error: {e}")
        
        end_time = time.time()
        total_duration = end_time - start_time
        
        self.generate_report(total_duration)
    
    def generate_report(self, total_duration):
        if not self.results:
            print("No results to report")
            return
        
        successful_requests = [r for r in self.results if r['success']]
        failed_requests = [r for r in self.results if not r['success']]
        
        total_requests = len(self.results)
        success_rate = (len(successful_requests) / total_requests) * 100 if total_requests > 0 else 0
        
        response_times = [r['response_time'] for r in successful_requests]
        
        print("\n" + "=" * 60)
        print("LOAD TEST RESULTS")
        print("=" * 60)
        print(f"Total Duration: {total_duration:.2f} seconds")
        print(f"Total Requests: {total_requests}")
        print(f"Successful Requests: {len(successful_requests)}")
        print(f"Failed Requests: {len(failed_requests)}")
        print(f"Success Rate: {success_rate:.2f}%")
        print(f"Requests per Second: {total_requests / total_duration:.2f}")
        
        if response_times:
            print(f"\nResponse Time Statistics:")
            print(f"Average: {statistics.mean(response_times):.3f}s")
            print(f"Median: {statistics.median(response_times):.3f}s")
            print(f"Min: {min(response_times):.3f}s")
            print(f"Max: {max(response_times):.3f}s")
            print(f"95th Percentile: {self.percentile(response_times, 95):.3f}s")
            print(f"99th Percentile: {self.percentile(response_times, 99):.3f}s")
        
        status_codes = {}
        for result in self.results:
            code = result['status_code']
            status_codes[code] = status_codes.get(code, 0) + 1
        
        print(f"\nStatus Code Distribution:")
        for code, count in sorted(status_codes.items()):
            print(f"  {code}: {count} ({(count/total_requests)*100:.1f}%)")
        
        if failed_requests:
            print(f"\nError Summary:")
            error_types = {}
            for result in failed_requests:
                error = result.get('error', 'Unknown error')
                error_types[error] = error_types.get(error, 0) + 1
            
            for error, count in error_types.items():
                print(f"  {error}: {count}")
    
    def percentile(self, data, percentile):
        if not data:
            return 0
        sorted_data = sorted(data)
        index = int((percentile / 100) * len(sorted_data))
        if index >= len(sorted_data):
            index = len(sorted_data) - 1
        return sorted_data[index]

def main():
    # TARGET_URL = "your_url" 
    NUM_USERS = 1000
    DURATION = 60
    REQUESTS_PER_USER = 5
    
    print("WordPress Load Testing Tool")
    print("=" * 30)
    
    try:
        num_users = int(input(f"Enter number of concurrent users (default {NUM_USERS}): ") or NUM_USERS)
        duration = int(input(f"Enter test duration in seconds (default {DURATION}): ") or DURATION)
        requests_per_user = int(input(f"Enter requests per user (default {REQUESTS_PER_USER}): ") or REQUESTS_PER_USER)
        target_url = input(f"Enter target URL (default {TARGET_URL}): ") or TARGET_URL
        
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url
        
        load_tester = LoadTester(
            target_url=target_url,
            num_users=num_users,
            duration=duration,
            requests_per_user=requests_per_user
        )
        
        print(f"\nWarning: This will generate heavy load on {target_url}")
        confirm = input("Continue? (y/N): ")
        
        if confirm.lower() == 'y':
            load_tester.run_load_test()
            show_credits()
        else:
            print("Load test cancelled.")
            
    except KeyboardInterrupt:
        print("\nLoad test interrupted by user.")
    except Exception as e:
        print(f"Error: {e}")

def show_credits():
    print("\n" + "=" * 50)
    print("Thanks for using this load testing tool!")
    print("If you found this useful, please:")
    print("⭐ Give this repository a star")
    print("👤 Follow @rafitojuan")
    print("=" * 50)

if __name__ == "__main__":
    main()