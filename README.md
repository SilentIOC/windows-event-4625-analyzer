# Windows Event ID 4625 – Failed Logon Analysis (SOC Lab)

## 📌 Overview
This project demonstrates hands-on Security Operations Center (SOC) log analysis by detecting and analyzing Windows Event ID 4625 (Failed Logon Attempts) using Python.

The lab simulates real-world SOC workflows such as log parsing, indicator extraction, authentication failure analysis, and analyst-style reporting.

This project aligns with **Tier 1 SOC Analyst responsibilities**, including:
- Authentication failure investigation
- Brute-force detection logic
- Log analysis and triage
- Incident documentation and reporting

---

## 🎯 Objective
Analyze Windows Security Event ID 4625 logs to identify failed logon activity and demonstrate SOC-style log analysis using Python automation.

---

## 🧪 Lab Environment
- Kali Linux (VirtualBox)
- Windows Security Event Logs (XML export)
- Python 3
- Git & GitHub

---

## 🛠️ Tools & Technologies
- Python (custom log analyzer)
- `xml.etree.ElementTree`
- Linux command-line tools
- Windows Security Event Logs (Event ID 4625)
- GitHub for version control

---

## 🔍 What the Script Does
The Python analyzer:
- Parses Windows Security log XML files
- Detects Event ID **4625** (failed logons)
- Extracts:
  - Target usernames
  - Source IP addresses
  - Logon types
  - Status & SubStatus codes
  - Event timestamps
- Generates a summarized SOC-style report

---

## 📊 Sample Findings
- Multiple failed logon attempts targeting `administrator` and `guest`
- Both network (LogonType 3) and remote interactive/RDP (LogonType 10) attempts
- Status codes indicating invalid credentials
- Clear indicators of potential brute-force behavior

---

## ▶️ How to Run
```bash
python3 win4625_analyzer.py
cat win4625_report.txt

