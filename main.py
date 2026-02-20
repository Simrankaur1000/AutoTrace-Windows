import platform
from browser import get_browser_history
from logins import get_failed_logins
import json

def main():
    os_type = platform.system()
    if os_type != "Windows":
        print("This version only works on Windows.")
        return

    print(f"Detected OS: {os_type}")

    history = get_browser_history()
    failed_logins = get_failed_logins()

    report = {
        "browser_history_last_30_days": history,
        "failed_logins_last_30_days": failed_logins
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("✅ JSON report generated successfully.")
    print("Output file: report.json")

if __name__ == "__main__":
    main()