# main.py
import argparse
import pandas as pd
from analyzer import parser, parser_evtx, detectors, exporter, visualizer, alerts

def main():
    parser_cli = argparse.ArgumentParser(description="Security Log Analyzer CLI Tool")
    parser_cli.add_argument("--log", required=True, help="Path to the log file")
    parser_cli.add_argument("--format", required=True, choices=["linux", "evtx"], help="Log format")
    parser_cli.add_argument("--output", choices=["csv", "sqlite"], help="Export format")
    parser_cli.add_argument("--visualize", action="store_true", help="Visualize failed login attempts")
    parser_cli.add_argument("--alert", action="store_true", help="Send alerts via email/Slack")
    
    args = parser_cli.parse_args()

    if args.format == "linux":
        df = parser.parse_auth_log(args.log)
    else:
        df = parser_evtx.parse_evtx(args.log)

    failed_logins = detectors.detect_failed_logins(df)
    invalid_users = detectors.detect_invalid_users(df)

    print("\n[+] Failed Login Attempts by IP:")
    print(failed_logins)

    print("\n[+] Invalid Users:")
    print(invalid_users)

    flagged_df = pd.DataFrame({
        "IP": failed_logins.index,
        "Failed_Attempts": failed_logins.values
    })

    if args.output == "csv":
        exporter.export_to_csv(flagged_df)
    elif args.output == "sqlite":
        exporter.export_to_sqlite(flagged_df)

    if args.visualize:
        visualizer.plot_failed_logins(failed_logins)

    if args.alert:
        message = f"Security Alert:\nFailed Logins:\n{failed_logins.head().to_string()}\nInvalid Users: {invalid_users}"
        alerts.send_email("Security Log Alert", message)
        alerts.send_slack(message)

if __name__ == "__main__":
    main()
