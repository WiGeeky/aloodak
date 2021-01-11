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
import argparse
from core import getPollutionData, Visualizor
from config import Config, MeasureTracker
from requests import post

if __name__ == '__main__':
    # Process passed arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Config file to be used')
    args = parser.parse_args()

    config_path = None if not args.config else args.config

    # Initialize classes
    config = Config(file_path=config_path)
    tracker = MeasureTracker(file_path=f'lm_{config.country}_{config.province}_{config.city}.conf.json')

    data = getPollutionData(config.iqair_api_key, config.country, config.province, config.city)
    info = Visualizor(data, True)

    if info.aqi != tracker.last_measure:
        info.generateImage()
        info.generateCaption()
        post(f'https://mikey.ir/bot{config.telegram_api_key}/sendPhoto', data={'chat_id': config.telegram_chat_id, 'caption': info.caption, 'disable_notifications': True}, files={'photo': info.imageb})
        tracker.setMeasure(info.aqi)