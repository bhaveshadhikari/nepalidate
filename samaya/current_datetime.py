from .converter import ad_to_bs
from datetime import datetime
import pytz

class DateTimeInfo:
    """Container for date/time information in both AD and BS formats."""
    
    def __init__(self, ad_date, bs_date, time, weekday):
        self.ad_date = ad_date
        self.bs_date = bs_date
        self.time = time
        self.weekday = weekday


def datetime_now():
    """Get current date and time in Nepal timezone with both AD and BS formats.
    
    Returns:
        DateTimeInfo: Object containing ad_date, bs_date, time, and weekday
    """
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
