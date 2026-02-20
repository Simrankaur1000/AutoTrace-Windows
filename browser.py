import os
import sqlite3
import shutil
import datetime
import tempfile

def get_browser_history():
    history_list = []
    user_home = os.path.expanduser("~")
    paths = [
        os.path.join(user_home, r"AppData\Local\Google\Chrome\User Data\Default\History"),
        os.path.join(user_home, r"AppData\Local\Microsoft\Edge\User Data\Default\History")
    ]

    for path in paths:
        if os.path.exists(path):
            tmp_db = os.path.join(tempfile.gettempdir(), "History_copy")
            try:
                shutil.copy2(path, tmp_db)
                conn = sqlite3.connect(tmp_db)
                cursor = conn.cursor()
                cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 1000")
                rows = cursor.fetchall()
                thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
                for row in rows:
                    url = row[0]
                    title = row[1]
                    timestamp = row[2]
                    try:
                        visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=timestamp)
                        if visit_time >= thirty_days_ago:
                            history_list.append({
                                "url": url,
                                "title": title,
                                "visit_time": visit_time.strftime("%Y-%m-%d %H:%M:%S")
                            })
                    except:
                        continue
            except Exception as e:
                print(f"Error reading {path}: {e}")
            finally:
                conn.close()
                os.remove(tmp_db)

    return history_list