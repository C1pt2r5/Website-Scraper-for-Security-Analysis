# monitor/watch_log.py
import time
import os
from analyzer.parser import parse_auth_log
from analyzer.parser_evtx import parse_evtx
from analyzer.detectors import detect_failed_logins

def start_monitoring(log_path, log_format):
    print(f"[+] Monitoring {log_path} for changes...")
    last_size = os.path.getsize(log_path)

    while True:
        try:
            current_size = os.path.getsize(log_path)
            if current_size > last_size:
                print("[*] New log entries detected. Analyzing...")
                if log_format == 'linux':
                    df = parse_auth_log(log_path)
                else:
                    df = parse_evtx(log_path)

                failed_ips = detect_failed_logins(df)
                if not failed_ips.empty:
                    print("[!] Failed login attempts:")
                    print(failed_ips.head())

                last_size = current_size

            time.sleep(5)
        except KeyboardInterrupt:
            print("[-] Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"[!] Error during monitoring: {e}")
