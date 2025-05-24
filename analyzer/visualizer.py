# analyzer/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_failed_logins(failed_logins_series):
    if failed_logins_series.empty:
        print("[-] No failed login data to plot.")
        return
    plt.figure(figsize=(10, 6))
    sns.barplot(x=failed_logins_series.values, y=failed_logins_series.index)
    plt.xlabel("Failed Attempts")
    plt.ylabel("IP Address")
    plt.title("Top Failed Login Attempts by IP")
    plt.tight_layout()
    plt.show()
