# analyzer/parser_evtx.py
import pandas as pd
from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET

def parse_evtx(filepath):
    data = []
    with Evtx(filepath) as log:
        for record in log.records():
            try:
                xml = ET.fromstring(record.xml())
                message = xml.find(".//EventData").text or ''
                data.append({'message': message})
            except Exception:
                continue
    return pd.DataFrame(data)
