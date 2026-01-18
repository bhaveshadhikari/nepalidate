import sys
from pathlib import Path

# Add the parent directory (project/) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data import TOTAL_BS_MONTHLY_DAYS, MONTH_START_WEEKDAY
from data import NEW_YEAR_BS_AD_MAP
from datetime import date, timedelta

def bs_to_ad(bs_date:str):
    # bs_date = "2080-9-30"
    year, month, day = bs_date.split("-")
    year, month, day = (int)(year), (int)(month), (int)(day)
    year_start_ad_date = NEW_YEAR_BS_AD_MAP[f'{year}']
    ad_year, ad_month, ad_day = year_start_ad_date.split('-')
    total_monthly_days_for_year = TOTAL_BS_MONTHLY_DAYS[year-2000]
    # print(total_monthly_days_for_year)
    month_idx = month - 1
    day_idx = day - 1
    if month_idx > 0 :
        days_offset_from_year_start = sum(total_monthly_days_for_year[0:month_idx])+day_idx
    else:
        days_offset_from_year_start = day_idx
        
    # print(days_offset_from_year_start)

    date_ad = date(int(ad_year), int(ad_month), int(ad_day)) + timedelta(days=days_offset_from_year_start)
    return date_ad

if __name__ == "__main__":
    print(bs_to_ad("2060-07-24"))