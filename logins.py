import win32evtlog
import datetime

def get_failed_logins():
    server = 'localhost'
    log_type = 'Security'
    failed_logins = []

    try:
        hand = win32evtlog.OpenEventLog(server, log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand, flags, 0)

        thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)

        for ev_obj in events:
            if ev_obj.EventID == 4625:  # 4625 = failed logon
                time = ev_obj.TimeGenerated
                if time >= thirty_days_ago:
                    failed_logins.append({
                        "user": ev_obj.StringInserts[5] if ev_obj.StringInserts else "N/A",
                        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "workstation": ev_obj.StringInserts[18] if len(ev_obj.StringInserts) > 18 else "N/A"
                    })
    except Exception as e:
        print(f"Error reading Windows Security Log: {e}")

    return failed_logins