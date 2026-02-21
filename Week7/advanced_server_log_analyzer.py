import logging
import re
from collections import defaultdict


#CONFIGURE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("analysis_audit.log"),
        logging.StreamHandler()
    ]
)

#PARSE REAL LOG LINES
LOG_PATTERN = re.compile(
    r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+)'
)

def parse_log_line(line, line_num):
    match = LOG_PATTERN.match(line)

    if not match:
        return None

    ip, timestamp, method, url, status, size = match.groups()

    return {
        "ip": ip,
        "timestamp": timestamp,
        "method": method,
        "url": url,
        "status": int(status),
        "size": int(size)
    }

def analyze_logs(input_file):
    """ANALYZE LOG ENTRY FOR SECURITY ISSUES"""
    total_requests = 0
    error_entries = []
    security_incidents = []
    failed_attempts = defaultdict(int)

    try:
        with open(input_file, "r") as f:
            for line_num, line in enumerate(f, 1):

                entry = parse_log_line(line.strip(), line_num)
                if not entry:
                    continue

                total_requests += 1

                #ERROR LOGS 4XX AND 5XX CODES
                if entry["status"] >= 400:
                    error_entries.append(entry)

                #FAILED AUTHENTIFICATION ATTEMPTS: BRUTE FORCE DETECTION
                if entry["url"] == "/login" and entry["status"] == 401:

                    failed_attempts[entry["ip"]] += 1

                if failed_attempts[entry["ip"]] == 3:
                    incident = (
                        f"Brute Force Attempt From {entry['ip']} "
                        f"({failed_attempts[entry['ip']]} Failed Attempts) "
                    )
                    security_incidents.append(incident)
                    logging.warning(incident)

                #SUSPICIOUS USER AGENTS
                if "curl" in line.lower() or "sqlmap" in line.lower():
                    incident = (
                        f"Suspicious Tool Detected From {entry['ip']} "
                        f"Using {entry['method']} {entry['url']}"
                    )
                    security_incidents.append(incident)
                    logging.warning(incident)

        logging.info(f"Processed {total_requests} Requests")

        return total_requests, error_entries, security_incidents

    except FileNotFoundError:
        logging.error(f"File Not Found: {input_file}")
        raise
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        raise

    #CREATE ERROR_LOG.TXT
def generate_error_log(errors):
    try:
        with open('error_log.txt', 'w') as f:
            f.write("=" * 70 + "\n" )
            f.write("HTTP ERRORS LOG\n ")
            f.write("=" * 70 + "\n\n")

            for entry in errors:
                f.write(
                    f"[{entry['timestamp']}] "
                    f"{entry['ip']} - "
                    f"{entry['method']} {entry['url']} "
                    f"(Status {entry['status']})\n"
                )

        logging.info("error_log.txt Generated")

    except PermissionError:
        logging.error("Cannot Write error_log.txt")

#CREATE SECURITY_INCIDENTS.TXT
def generate_security_report(incidents):
    try:
        with open('security_incidents.txt', 'w') as f:
            f.write("=" * 70 + "\n" )
            f.write("SECURITY INCIDENTS REPORT\n ")
            f.write("=" * 70 + "\n\n")

            f.write(f'Total Incidents: {len(incidents)}\n\n')

            for incident in incidents:
                f.write(f"{incident}\n")

        logging.info("security_incidents.txt Generated")

    except PermissionError:
        logging.error("Cannot Write security_incidents.txt")

def main():
    input_file = "server.log"

    try:
        total, errors, incidents = analyze_logs(input_file)

        generate_error_log(errors)
        generate_security_report(incidents)

        print("\nAdvanced Server Log Analysis Complete.")
        print(f"Total Requests Processed: {total}")
        print(f"Errors Identified: {len(errors)}")
        print(f"Security Incidents Identified: {len(incidents)}")

    except Exception as e:
        print(f"Analysis Failed: {e}")

if __name__ == "__main__":
    main()