#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime

INPUT_FILE = "security_4625.xml"
OUTPUT_FILE = "win4625_report.txt"

def main():
    try:
        tree = ET.parse(INPUT_FILE)
    except FileNotFoundError:
        print(f"[!] Input file {INPUT_FILE} not found.")
        return

    root = tree.getroot()

    events = root.findall(".//Event")
    usernames = Counter()
    ip_addresses = Counter()
    logon_types = Counter()
    statuses = Counter()
    substatuses = Counter()
    samples = []

    for event in events:
        event_id = event.find(".//EventID")
        if event_id is None or event_id.text != "4625":
            continue

        data = {d.attrib["Name"]: d.text for d in event.findall(".//Data")}

        usernames[data.get("TargetUserName", "UNKNOWN")] += 1
        ip_addresses[data.get("IpAddress", "UNKNOWN")] += 1
        logon_types[data.get("LogonType", "UNKNOWN")] += 1
        statuses[data.get("Status", "UNKNOWN")] += 1
        substatuses[data.get("SubStatus", "UNKNOWN")] += 1

        if len(samples) < 5:
            samples.append({
                "time": event.find(".//TimeCreated").attrib.get("SystemTime"),
                "user": data.get("TargetUserName"),
                "ip": data.get("IpAddress"),
                "logon_type": data.get("LogonType"),
                "status": data.get("Status"),
                "substatus": data.get("SubStatus")
            })

    with open(OUTPUT_FILE, "w") as f:
        f.write("Windows Failed Logon Analyzer (Event ID 4625)\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        f.write("Top TargetUserName (attempt counts)\n")
        for user, count in usernames.most_common():
            f.write(f"{count} {user}\n")

        f.write("\nTop Source IpAddress (attempt counts)\n")
        for ip, count in ip_addresses.most_common():
            f.write(f"{count} {ip}\n")

        f.write("\nLogonType distribution\n")
        for lt, count in logon_types.items():
            f.write(f"{count} {lt}\n")

        f.write("\nStatus distribution\n")
        for st, count in statuses.items():
            f.write(f"{count} {st}\n")

        f.write("\nSubStatus distribution\n")
        for sst, count in substatuses.items():
            f.write(f"{count} {sst}\n")

        f.write("\nSample Events\n")
        for s in samples:
            f.write(
                f"time={s['time']} user={s['user']} ip={s['ip']} "
                f"logon_type={s['logon_type']} status={s['status']} "
                f"substatus={s['substatus']}\n"
            )

    print(f"[+] Report written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
