import re

# File paths for logs
LOG_FILE = "system_logs.txt"  # Path to the log file

# Function to parse logs and detect security events
def parse_logs():
    security_events = []
    
    with open(LOG_FILE, 'r') as log_file:
        for line in log_file:
            # Detect failed login attempts
            if re.search(r'Failed password', line):
                security_events.append(f"Failed login attempt: {line.strip()}")
            
            # Detect unauthorized access
            if re.search(r'authentication failure', line):
                security_events.append(f"Unauthorized access attempt: {line.strip()}")
            
            # Detect system reboots
            if re.search(r'reboot', line):
                security_events.append(f"System reboot detected: {line.strip()}")

    return security_events

# Function to generate a simple report
def generate_report(events):
    with open('siem_report.txt', 'w') as report_file:
        report_file.write("SIEM Security Events Report\n")
        report_file.write("===========================\n\n")
        if events:
            for event in events:
                report_file.write(event + '\n')
        else:
            report_file.write("No security events detected.\n")

# Main SIEM function
def run_siem():
    print("Collecting logs...")
    events = parse_logs()
    print("Generating report...")
    generate_report(events)
    print("Report generated: siem_report.txt")

# Run the SIEM tool
if __name__ == "__main__":
    run_siem()
