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
- Primary source IP: **127.0.0.1**
- Logon type observed: **Type 2 (Interactive)**
- Status code: **0xc000006d**
- SubStatus code: **0xc0000380**

## Security Interpretation
The repeated failed logon attempts indicate unsuccessful authentication activity.  
While the source IP suggests local testing, similar patterns in production environments may indicate:
- Password guessing
- Brute-force attempts
- Misconfigured services

## Outcome
This lab demonstrates the ability to:
- Parse Windows security logs
- Detect authentication failures
- Translate raw log data into actionable SOC insights
- Document findings in a professional incident-style report

## Next Steps
- Add support for additional Event IDs
- Export results to CSV
- Correlate failed and successful logon events
# Windows Event ID 4625 Analyzer

Week 1 SOC Lab  
Author: Julio Betancourt

This project analyzes Windows Security Event ID 4625 (failed logon attempts)
and summarizes attack indicators for SOC analysis.
