# Nepali Date Converter

## Features

- Convert dates between Gregorian (AD) and Nepali (BS) calendars
- Generate Real Time both AD and BS dates simultaneously

## Library Usage

1. Clone the repository:
   ```bash
   git clone --branch converter git@github.com:bhaveshadhikari/nepalidate.git
   
   ```

```python
from nepalidate.converter import ad_to_bs, bs_to_ad
from nepalidate.current_datetime import datetime_now
   print(ad_to_bs('2025-10-02'))

   dt=datetime_now()
    print(dt.ad_date)
    print(dt.bs_date)
    print(dt.time)
    print(dt.weekday)

ad_to_bs('yyyy-mm-dd') // returns 'yyyy-mm-dd' in bs 
bs_to_ad('yyyy-mm-dd') // returns 'yyyy-mm-dd' in ad 
```