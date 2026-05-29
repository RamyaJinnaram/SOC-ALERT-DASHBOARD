from collections import defaultdict

def detect_threats(log_file):
failed_attempts = defaultdict(int)

```
with open(log_file, "r") as file:
    logs = file.readlines()

alerts = []

for log in logs:
    ip, status = log.strip().split()

    if status == "FAILED":
        failed_attempts[ip] += 1

for ip, count in failed_attempts.items():
    if count >= 3:
        alerts.append(f"ALERT: Suspicious activity from {ip} (Failed: {count})")

return alerts
```
