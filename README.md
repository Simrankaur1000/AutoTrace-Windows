# AutoTrace-Windows

Windows-only Digital Forensics (DF) tool to collect user activity for the last 30 days.

---

## Features

- Collect **Chrome** and **Edge** browser history (last 30 days)
- Collect **failed login attempts** (last 30 days)
- Output is stored in a **JSON file**
- Works only on **Windows** (requires Administrator to read Security Logs)

---

## Requirements

- Python 3.10+
- Windows OS
- Closed browsers (Chrome and Edge)
- Administrator privileges to read Security Event Logs

### Python dependencies

Install dependencies with:

```powershell/cmd
git-clone https://github.com/Simrankaur1000/AutoTrace-Windows.git
cd AutoTrace-Windows
pip install -r requirements.txt
python main.py
