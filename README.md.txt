Simplified SIEM Tool
Overview
I created this basic SIEM (Security Information and Event Management) tool to showcase how security events can be detected from logs. The tool reads log files, identifies potential security issues like failed login attempts and system reboots, and generates a simple report. This is a lightweight implementation designed to give a clear idea of how SIEM tools work in practice.

Features
Log Parsing: The tool reads system logs from a specified log file.
Event Detection: It identifies common security events like:
Failed login attempts
Unauthorized access attempts
System reboots
Report Generation: Detected security events are written to a report for review.
How to Run the Tool
Place your log file in the same directory as the simple_siem.py script. I’ve included a sample log file, system_logs.txt, for testing purposes.
To run the tool, open a Command Prompt, navigate to the project directory, and execute:
python simple_siem.py
The tool will generate a siem_report.txt file, which contains a summary of the detected security events.

SIEM Security Events Report
===========================

Failed login attempt: Feb 10 10:23:12 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2
Unauthorized access attempt: Feb 10 10:24:15 server sshd[1234]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.100  user=root
System reboot detected: Feb 10 10:25:20 server systemd[1]: Starting reboot.target...
Why I Built This
I wanted to create a simple tool that could simulate the core functionalities of a SIEM system, providing insight into how log analysis and event detection work in cybersecurity. The idea was to build a quick, practical tool that collects logs, parses them for common security events, and generates a report that could be useful for identifying potential security issues.