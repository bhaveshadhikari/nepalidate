from .data import TOTAL_BS_MONTHLY_DAYS, MONTH_START_WEEKDAY
from .data import NEW_YEAR_BS_AD_MAP
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


def ad_to_bs(ad_date:str):
    # ad_date = "2016-05-18"
    year, month, day = ad_date.split("-")
    year, month, day = (int)(year), (int)(month), (int)(day)

    # 1951-06-14 -> base: 1951-04-14
    # 1951-03-21 -> base: 1950-04-14
    year_idx = year - 1943
    year_start_ad_base_date = list(NEW_YEAR_BS_AD_MAP.items())[year_idx]
    if date.fromisoformat(year_start_ad_base_date[1]) > date.fromisoformat(ad_date):
        year_start_ad_base_date = list(NEW_YEAR_BS_AD_MAP.items())[year_idx-1]


    difference =  date.fromisoformat(ad_date)-date.fromisoformat(year_start_ad_base_date[1])
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

    return(f"{bs_base_year}-{bs_month}-{bs_day}")

if __name__ == "__main__":
    print(bs_to_ad("2060-07-24"))