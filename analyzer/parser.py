import pandas as pd
import re
from datetime import datetime

def parse_auth_log(filepath):
    log_pattern = re.compile(r'(?P<month>\w+) +(?P<day>\d+) (?P<time>\S+) (?P<host>\S+) (?P<process>\S+): (?P<message>.*)')
    data = []

    with open(filepath, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                entry = match.groupdict()
                entry['timestamp'] = datetime.strptime(
                    f"{entry['month']} {entry['day']} {entry['time']}", "%b %d %H:%M:%S"
                )
                data.append(entry)

    return pd.DataFrame(data)
