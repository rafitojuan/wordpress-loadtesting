# 🚀 WordPress Load Testing Tool

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> 💪 A powerful and comprehensive load testing tool designed specifically for WordPress websites

## 🌟 Features

- 🎯 **WordPress Optimized**: Specifically designed for testing WordPress sites
- ⚡ **High Performance**: Test with up to 1000+ concurrent users
- 📊 **Detailed Analytics**: Comprehensive reporting with response times and success rates
- 🔧 **Configurable**: Easily adjust users, duration, and requests per user
- 📈 **Real-time Monitoring**: Live progress tracking during tests
- 🛡️ **Error Analysis**: Detailed breakdown of failed requests
- 🎨 **User-friendly**: Interactive prompts for easy configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- `requests` library

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd stresstest
```

2. Install required dependencies:
```bash
pip install requests
```

### Usage

#### Python Version
```bash
python loadtest.py
```

#### JavaScript Version
```bash
node loadtest.js
```

## ⚙️ Configuration

The tool provides interactive prompts for configuration:

- 👥 **Number of concurrent users** (default: 1000)
- ⏱️ **Test duration** in seconds (default: 60)
- 🔄 **Requests per user** (default: 5)
- 🌐 **Target URL** (default: https://antartiket.com)

## 📊 Sample Output

```
WordPress Load Testing Tool
==============================

🚀 Starting load test...
Target: https://antartiket.com
Users: 1000
Duration: 60 seconds
Requests per user: 5

📈 Progress: [████████████████████] 100%

📋 Load Test Results:
==============================
Total Requests: 5000
Successful Requests: 4850 (97.0%)
Failed Requests: 150 (3.0%)
Average Response Time: 245.67 ms
Median Response Time: 198.23 ms
95th Percentile: 567.89 ms
Requests per Second: 83.33
```

## 🎯 Use Cases

- 🔍 **Performance Testing**: Identify bottlenecks in your WordPress site
- 📈 **Capacity Planning**: Determine maximum user load your server can handle
- 🛠️ **Optimization Validation**: Test improvements after optimization
- 🚨 **Stress Testing**: Push your server to its limits safely
- 📊 **Baseline Metrics**: Establish performance benchmarks

## ⚠️ Important Notes

- 🚨 **Use Responsibly**: Only test websites you own or have permission to test
- 🌐 **Network Impact**: High concurrent users may impact network performance
- 💻 **Server Resources**: Monitor your target server during testing
- 📋 **Legal Compliance**: Ensure testing complies with terms of service

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

If you found this tool useful:
- ⭐ **Star this repository**
- 👤 **Follow [@rafitojuan](https://github.com/rafitojuan)**

## 📞 Support

If you encounter any issues or have questions:
- 🐛 [Report bugs](../../issues)
- 💡 [Request features](../../issues)
- 📧 Contact the maintainer

---

<div align="center">
  <strong>Made with ❤️ for the WordPress community</strong>
</div>