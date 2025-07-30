import http from "k6/http";

export let options = {
  vus: 1000, // virtual users
  duration: "30s",
};

export default function () {
  // http.get("your_url");
}