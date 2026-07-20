An Apache-style access log is available at /app/access.log in the working directory. Parse it and write a JSON summary of the traffic.

Write your report to the absolute path /app/report.json. It must be a single JSON object with exactly these three keys:

- "total_requests": the total number of request lines in the log (integer)
- "unique_ips": the number of distinct client IP addresses, read from the first whitespace-separated field of each line (integer)
- "top_path": the request path that appears most often, read from the quoted request line (for example the line `"GET /index.html HTTP/1.1"` has path `/index.html`) (string)

Success criteria:
1. A single JSON object is written to /app/report.json.
2. "total_requests" equals the number of request lines in the log.
3. "unique_ips" equals the number of distinct client IP addresses.
4. "top_path" equals the most frequently requested path.
