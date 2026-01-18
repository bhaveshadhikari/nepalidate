from .converter import ad_to_bs
from datetime import datetime
import pytz

class DateTimeInfo:
    def __init__(self, ad_date, bs_date, time, weekday):
        self.ad_date = ad_date
        self.bs_date = bs_date
        self.time = time
        self.weekday = weekday

def datetime_now():
    nepal_tz = pytz.timezone('Asia/Kathmandu')
    ad_datetime_now = datetime.now(nepal_tz)
    ad_date = ad_datetime_now.strftime("%Y-%m-%d")
    time = ad_datetime_now.strftime("%H:%M:%S")
    weekday = ad_datetime_now.strftime("%A")
    bs_date = ad_to_bs(ad_date)

    return DateTimeInfo(
        ad_date,
        bs_date,
        time,
        weekday
    )

if __name__ == '__main__':
    dt=datetime_now()
    print(dt.ad_date)
    print(dt.bs_date)
    print(dt.time)
    print(dt.weekday)

    