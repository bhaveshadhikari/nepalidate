# Samaya - Nepali Date and Time
A lightweight Python library for BS/AD date conversion and calendar utilities.
## Features

- Convert dates between Gregorian (AD) and Nepali (BS) calendars
- Get current date and time in both AD and BS formats with Nepal timezone
- Lightweight with minimal dependencies (only `pytz`)
- Support for BS years 2000-2099

## Installation

Install from PyPI:
```bash
pip install samaya
```

Or install locally in development mode:
```bash
git clone https://github.com/bhaveshadhikari/samaya.git
cd samaya
pip install -e .
```

## Usage

### Basic Date Conversion

```python
from samaya import ad_to_bs, bs_to_ad

# Convert AD to BS
bs_date = ad_to_bs('2025-10-02')
print(bs_date)  # Output: 2082-6-17

# Convert BS to AD
ad_date = bs_to_ad('2082-06-17')
print(ad_date)  # Output: 2025-10-2
```

### Get Current Date and Time

```python
from samaya import datetime_now

dt = datetime_now()
print(dt.ad_date)   # Gregorian date (e.g., 2025-10-02)
print(dt.bs_date)   # Nepali date (e.g., 2082-06-17)
print(dt.time)      # Current time in Nepal timezone
print(dt.weekday)   # Day of week (e.g., Thursday)
```

## API Reference

### `ad_to_bs(ad_date: str) -> str`
Convert a Gregorian date to Nepali date.
- **Parameters**: `ad_date` - Date string in format 'YYYY-MM-DD'
- **Returns**: Date string in format 'YYYY-MM-DD' (BS)

### `bs_to_ad(bs_date: str) -> str`
Convert a Nepali date to Gregorian date.
- **Parameters**: `bs_date` - Date string in format 'YYYY-MM-DD'
- **Returns**: Date string in format 'YYYY-MM-DD' (AD)

### `datetime_now() -> DateTimeInfo`
Get current date and time in both formats.
- **Returns**: DateTimeInfo object with properties:
  - `ad_date`: Current Gregorian date
  - `bs_date`: Current Nepali date
  - `time`: Current time in HH:MM:SS format
  - `weekday`: Current day of week

## Requirements

- Python >= 3.7
- pytz >= 2021.1

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.