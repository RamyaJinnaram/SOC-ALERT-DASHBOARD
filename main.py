from collections import defaultdict

failed_attempts = defaultdict(int)

with open("logs.txt", "r") as file:
    logs = file.readlines()

print("=== SOC ALERT DASHBOARD ===\n")

for log in logs:
    ip, status = log.strip().split()

    if status == "FAILED":
        failed_attempts[ip] += 1

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"ALERT: Suspicious activity detected from IP {ip}")
        print(f"Failed Attempts: {count}\n")
        


