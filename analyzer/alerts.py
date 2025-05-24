# analyzer/alerts.py
import smtplib
import requests
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def send_email(subject, body):
    config = load_config()["email"]
    msg = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(config["from"], config["password"])
            server.sendmail(config["from"], config["to"], msg)
        print("[+] Email alert sent.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

def send_slack(message):
    webhook_url = load_config()["slack"]["webhook_url"]
    try:
        response = requests.post(webhook_url, json={"text": message})
        if response.status_code == 200:
            print("[+] Slack alert sent.")
        else:
            print(f"[!] Slack alert failed: {response.text}")
    except Exception as e:
        print(f"[!] Slack alert error: {e}")
