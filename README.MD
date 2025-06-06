# Security Log Analyzer

Security Log Analyzer is a Python-based CLI tool that detects anomalies in Linux and Windows logs such as repeated failed logins, unauthorized access, and other suspicious activity.

## 🚀 Features

* Parse Linux (`auth.log`) and Windows EVTX logs
* Detect failed login attempts and invalid users
* Export results to CSV or SQLite
* Visualize failed login patterns with matplotlib/seaborn
* Send alerts via Email and Slack
* Real-time monitoring of logs

## 🛠 Installation

```bash
pip install .
```

## 🔧 Usage

```bash
log-analyzer --log /path/to/log --format linux --output csv --visualize --alert
```

### Arguments:

* `--log`: Path to the log file
* `--format`: `linux` or `evtx`
* `--output`: `csv` or `sqlite`
* `--visualize`: (Optional) Show plot of failed logins
* `--alert`: (Optional) Send email/Slack alert

## ⚙ Configuration

Edit `config.json` to set email and Slack webhook credentials:

```json
{
  "email": {
    "from": "youremail@example.com",
    "password": "your_app_password",
    "to": "recipient@example.com"
  },
  "slack": {
    "webhook_url": "https://hooks.slack.com/services/XXX"
  }
}
```

## 🧱 Dependencies

* pandas
* matplotlib
* seaborn
* requests
* python-evtx

## 📄 License

See [LICENSE](LICENSE).

---

Made with ❤️ for cybersecurity monitoring.
#   W e b s i t e - S c r a p e r - f o r - S e c u r i t y - A n a l y s i s 
 
 
