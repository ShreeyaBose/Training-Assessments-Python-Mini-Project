
# Training-Assessments-Mini-Projects

OpsBot – Server Log Security Scanner

OpsBot is a Python-based automation tool designed to help IT operations teams efficiently monitor server logs and detect potential security threats.Instead of manually scanning thousands of log entries, OpsBot automatically filters critical events like:
1. CRITICAL system failures
2. ERROR messages
3. FAILED LOGIN attempts
It generates a summarized security report and a filtered alert file, saving time and improving accuracy.

Problem Statement: An IT team processes 5,000 log lines daily and spends 2+ hours manually identifying security issues such as failed login attempts.

OpsBot automates this process by:
1. Eliminating manual effort
2. Reducing human error
3. Providing instant insights

Features:
1. File Parsing: Reads server log files line-by-line
2. Pattern Matching: Detects: CRITICAL, ERROR, FAILED LOGIN
3. Data Structuring: Counts occurrences of each alert type
4. Report Generation: Creates a filtered alert file
5. File Verification: Displays output file size after processing
6. GUI Interface (Tkinter): Easy file selection and execution

Tech Stack: Python 

Built-in Libraries:
1. `re` (Regular Expressions)
2. `os` (File handling)
3. `datetime` (Timestamping)
4. `tkinter` (GUI)

Project Structure

```
OpsBot/
│── opsbot.py              # Main Python script
│── server.log            # Input log file
│── security_alert_*.txt  # Generated output file
│── README.md             # Project documentation
```

How to Run: 
1. Clone or Download
```bash
git clone https://github.com/your-username/OpsBot.git
cd OpsBot
```
2. Run the Script

```bash
python opsbot.py
```
3. Use the GUI
a. Click "Browse Log File"
b. Select `server.log`
c. Click "Run OpsBot"

Input Example:

Before Log- server.log:

```
2026-04-22 09:01:10 ERROR Database connection failed
2026-04-22 09:03:20 FAILED LOGIN attempt from 203.45.22.1
2026-04-22 09:05:33 CRITICAL Disk failure detected
2026-04-22 09:06:01 INFO Backup completed
```

Output Example: 

After Log- security_alert_2026-04-22.txt

```
2026-04-22 09:01:10 ERROR Database connection failed
2026-04-22 09:03:20 FAILED LOGIN attempt from 203.45.22.1
2026-04-22 09:05:33 CRITICAL Disk failure detected
```

Summary Popup:

```
CRITICAL      : 1
ERROR         : 1
FAILED LOGIN  : 1

Alert File Created: security_alert_2026-04-22.txt
File Size: 245 bytes
```
How It Works:

1. User selects a log file via GUI
2. Script scans each line using regex
3. Filters only critical security events
4. Counts occurrences using a dictionary
5. Writes filtered logs to a new file
6. Displays summary and file size

Output:



















































