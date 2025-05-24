# analyzer/detectors.py
import pandas as pd
import re

def detect_failed_logins(df):
    failed_pattern = re.compile(r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>[\d.]+)")
    failed_ips = {}

    for message in df['message']:
        match = failed_pattern.search(message)
        if match:
            ip = match.group('ip')
            failed_ips[ip] = failed_ips.get(ip, 0) + 1

    return pd.Series(failed_ips).sort_values(ascending=False)

def detect_invalid_users(df):
    invalid_users = set()
    for message in df['message']:
        if "invalid user" in message:
            parts = message.split()
            if "user" in parts:
                try:
                    idx = parts.index("user")
                    invalid_users.add(parts[idx + 1])
                except IndexError:
                    continue
    return list(invalid_users)
