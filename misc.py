""" Aloodak
    Copyright (C) 2021  Frowzy et al

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    For copyright related issues, contact frowzyispenguin<at>riseup.net
"""
import pytz
from datetime import datetime, time
import jdatetime

jdatetime.set_locale("fa_IR")

def now():
    tz = pytz.timezone('Asia/Tehran') 
    tehran_now = datetime.now(tz)    
    return tehran_now.strftime("%H:%M")


def today():
    today = jdatetime.datetime.now(pytz.timezone("Asia/Tehran")).strftime("%A %y/%m/%d").split()
    date = today[-1]
    today.pop(-1)
    day = " ".join(i.strip() for i in today)
    return [day, date]


def toPersianNumerics(string: str):
    digits = {'1':'۱', '2':'۲', '3':'۳', '4':'۴', '5':'۵', '6':'۶', '7':'۷', '8':'۸', '9':'۹', '0':'۰'}
    string = str(string) # In case a number is being passed

    # Map the string into a list, replace a character if there's a digit
    chars = list(map(lambda x: digits[x] if x.isdecimal() else x,list(string)))
    
    # Join the mapped string back together and return a string
    return ''.join([str(x) for x in chars]) 