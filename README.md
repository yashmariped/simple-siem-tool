🚨 Simple SIEM Tool 🚨
Welcome to the Simple SIEM (Security Information and Event Management) Tool! This tool is designed to simulate basic SIEM functionalities by collecting logs, detecting security events, and generating reports. It’s a great starting point to understand how SIEM systems work.

🔍 Overview
This project showcases a basic SIEM tool that parses system logs, identifies common security issues such as failed login attempts, unauthorized access, and system reboots, and generates a simple security report. It’s designed to demonstrate the fundamentals of log analysis and security monitoring.

🚀 Features
Log Parsing: Reads logs from a file and extracts security-related events.
Event Detection: Detects failed login attempts, unauthorized access, and system reboots.
Report Generation: Creates a report of detected events in a simple, readable format.
🛠️ How to Run
Clone this repository to your local machine:
git clone https://github.com/yashmariped/simple-siem-tool.git

Navigate to the project directory:
cd simple-siem-tool

Ensure you have a log file named system_logs.txt in the directory (sample included), or use your own system logs.

Run the SIEM tool:
python simple_siem.py

Check the generated report in the file siem_report.txt for the detected security events.

📝 Example Report
Here’s an example of what the output report will look like:

SIEM Security Events Report
Failed login attempt: Feb 10 10:23:12 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2
Unauthorized access attempt: Feb 10 10:24:15 server sshd[1234]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.100 user=root
System reboot detected: Feb 10 10:25:20 server systemd[1]: Starting reboot.target...

🤔 Why I Built This
I created this project to provide a simple but effective introduction to SIEM systems, focusing on log parsing and event detection. It’s a practical, hands-on way to see how basic cybersecurity monitoring works!

💻 Technologies Used
Python: For scripting and log analysis
Regex: For parsing logs and identifying key events
📫 How to Reach Me
Feel free to reach out if you have any questions or suggestions!
✉️ Email: yashcyberanalyst@gmail.com
🔗 LinkedIn
