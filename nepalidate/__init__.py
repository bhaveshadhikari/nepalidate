"""Nepali Date - Convert and get real time AD and BS date """

from .converter import ad_to_bs, bs_to_ad
from .current_datetime import datetime_now, DateTimeInfo

__version__ = "0.1.0"
__author__ = "Bhavesh Adhikari"
__all__ = ["ad_to_bs", "bs_to_ad", "datetime_now", "DateTimeInfo"]
