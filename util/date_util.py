import datetime
import platform

WINDOWS_DATE_TIME_STR = '%#m/%#d/%Y'
LINUX_DATE_TIME_STR = '%-m/%-d/%Y'

# https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
def is_windows() -> bool:
    return 'Windows' == platform.system()

def get_date_string() -> str:
    if is_windows():
        return WINDOWS_DATE_TIME_STR
    return LINUX_DATE_TIME_STR

def get_days_ago(base_date: datetime.date, days_ago: int) -> datetime.date:
    return base_date - datetime.timedelta(days=days_ago)


