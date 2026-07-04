from pathlib import Path


LOG_FILE = Path("python-practice/sample_login_logs.txt")
THRESHOLD = 3


def detect_failed_logins(log_file):
    failed_counts = {}

    with log_file.open("r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) != 4:
                continue

            timestamp = parts[0]
            ip_address = parts[1]
            username = parts[2]
            status = parts[3]

            if status == "FAILED":
                if ip_address not in failed_counts:
                    failed_counts[ip_address] = 0

                failed_counts[ip_address] += 1

    return failed_counts


def print_suspicious_ips(failed_counts):
    found = False

    for ip_address, count in failed_counts.items():
        if count >= THRESHOLD:
            found = True
            print(f"Suspicious IP: {ip_address}")
            print(f"Failed attempts: {count}")
            print()

    if not found:
        print("No suspicious IPs found.")


def main():
    failed_counts = detect_failed_logins(LOG_FILE)
    print_suspicious_ips(failed_counts)


if __name__ == "__main__":
    main()
