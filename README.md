# Windows Event ID 4625 – Failed Logon Analysis (SOC Lab)

## Objective
Analyze Windows Security Event ID 4625 logs to identify failed logon activity and demonstrate SOC-style log analysis using Python.

## Environment
- Kali Linux (VirtualBox)
- Windows Security Event Logs (.evtx)
- Python 3
- Git & GitHub

## Data Source
- Windows Security Log
- Event ID: 4625 (Failed Logon)

## Tools Used
- Python (custom log analyzer)
- xml.etree.ElementTree
- Linux CLI
- GitHub

## Analysis Summary
A Python script was used to parse exported Windows Security logs and identify failed authentication attempts.  
The script extracted:
- Target usernames
- Source IP addresses
- Logon types
- Status and SubStatus codes
- Event timestamps

## Key Findings
- Total failed logon events detected: **3**
- Primary source IP: *
# Windows Event ID 4625 – Failed Logon Analyzer (SOC Lab)

## 📌 Overview
This project demonstrates hands-on Security Operations Center (SOC) log analysis by detecting and analyzing **Windows Event ID 4625 (Failed Logon Attempts)** using Python.  
The goal is to simulate real-world SOC workflows such as log parsing, IOC extraction, and reporting.

This lab aligns with **SOC Analyst Tier 1 responsibilities**, including:
- Authentication failure analysis
- Brute-force detection logic
- Incident triage and reporting

---

## 🛠️ Tools & Technologies
- Python 3
- Windows Security Event Logs (XML)
- Linux (Kali)
- Git & GitHub
- Command-line log analysis

---

## 🔍 What the Script Does
The Python analyzer:
- Parses Windows Security logs (XML)
- Detects Event ID **4625**
- Extracts:
  - Target usernames
  - Source IP addresses
  - Logon types
  - Status & substatus codes
- Produces a summarized SOC-style report

---

## 📂 Repository Structure

---

## ▶️ How to Run
```bash
python3 win4625_analyzer.py
cat win4625_report.txt
