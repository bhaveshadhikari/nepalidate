from .data import TOTAL_BS_MONTHLY_DAYS, MONTH_START_WEEKDAY
from .data import NEW_YEAR_BS_AD_MAP
from datetime import date, timedelta

def bs_to_ad(bs_date: str):
    """Convert Bikram Sambat (BS) date to Gregorian (AD) date.
    
    Args:
        bs_date (str): Date string in format 'YYYY-MM-DD'
    
    Returns:
        str: Gregorian date in format 'YYYY-MM-DD'
    """
    year, month, day = bs_date.split("-")
    year, month, day = int(year), int(month), int(day)
    year_start_ad_date = NEW_YEAR_BS_AD_MAP[f'{year}']
    ad_year, ad_month, ad_day = year_start_ad_date.split('-')
    total_monthly_days_for_year = TOTAL_BS_MONTHLY_DAYS[year-2000]
    
    month_idx = month - 1
    day_idx = day - 1
    if month_idx > 0:
        days_offset_from_year_start = sum(total_monthly_days_for_year[0:month_idx]) + day_idx
    else:
        days_offset_from_year_start = day_idx
    
    date_ad = date(int(ad_year), int(ad_month), int(ad_day)) + timedelta(days=days_offset_from_year_start)
    return f"{date_ad.year}-{date_ad.month}-{date_ad.day}"


def ad_to_bs(ad_date: str):
    """Convert Gregorian (AD) date to Bikram Sambat (BS) date.
    
    Args:
        ad_date (str): Date string in format 'YYYY-MM-DD'
    
    Returns:
        str: Bikram Sambat date in format 'YYYY-MM-DD'
    """
    year, month, day = ad_date.split("-")
    year, month, day = int(year), int(month), int(day)

    year_idx = year - 1943
    year_start_ad_base_date = list(NEW_YEAR_BS_AD_MAP.items())[year_idx]
    if date.fromisoformat(year_start_ad_base_date[1]) > date.fromisoformat(ad_date):
        year_start_ad_base_date = list(NEW_YEAR_BS_AD_MAP.items())[year_idx-1]

    difference = date.fromisoformat(ad_date) - date.fromisoformat(year_start_ad_base_date[1])
    days_offset_from_year_start = difference.days

    bs_base_year = int(year_start_ad_base_date[0])
    total_monthly_days = TOTAL_BS_MONTHLY_DAYS[bs_base_year-2000]

    bs_month, bs_day = 0, 0
    remaining_days = days_offset_from_year_start
    for idx, total_days in enumerate(total_monthly_days):
        if remaining_days > total_days:
            remaining_days -= total_days
        else:
            bs_month, bs_day = idx+1, remaining_days+1
            break

    return f"{bs_base_year}-{bs_month}-{bs_day}"
