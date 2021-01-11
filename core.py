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
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests
from misc import now, today, toPersianNumerics

statusbar = {
    "Hazardous": "خطر اضطراری",
    "Very Unhealthy": "خیلی ناسالم",
    "Unhealthy": "ناسالم",
    "Unhealthy for Sensitive Groups": "ناسالم برای گروه های حساس",
    "Moderate": "سالم",
    "Good": "پاک"
}

# defining textcolor / light/dark colors has calculated by hps
color = {
    "Hazardous": (104,62,81),
    "Very Unhealthy": (99,70,117),
    "Unhealthy": (175,44,59),
    "Unhealthy for Sensitive Groups": (178,88,38),
    "Moderate": (165,127,35),
    "Good": (113,139,58)
}


def aqiToStatus(aqi: int):
    scale = [
        {'title': 'Hazardous', 'min': 300},
        {'title': 'Very Unhealthy', 'min': 201},
        {'title': 'Unhealthy', 'min': 151},
        {'title': 'Unhealthy for Sensitive Groups', 'min': 101},
        {'title': 'Moderate', 'min': 51},
        {'title': 'Good',  'min': 0},
    ]

    for status in scale:
        if aqi >= status['min']:
            return status['title']


def getPollutionData(iqair_key, country, province, city):
    url = f"http://api.airvisual.com/v2/city?city={city}&state={province}&country={country}&key={iqair_key}"
    json_results = requests.get(url).json() 
    # TODO write a fail-safe mechanism to stop the bot and log the incident.
    return json_results['data']


class Visualizor():
    def __init__(self, data: dict, manualCall=False):
        
        self.font = ImageFont.truetype("assets/fonts/Sahel-Black.ttf", 140) # rate font style

        
        self.temperature = data['current']['weather']['tp']
        self.humidity = data['current']['weather']['hu']
        self.aqi = data['current']['pollution']['aqius']
        self.status = aqiToStatus(self.aqi)
        self.status_text = statusbar[aqiToStatus(self.aqi)]
        self.color = color[self.status]

        self.imgdir = f"assets/badges/{self.status}.png"

        if not manualCall:
            self.generateCaption()
            self.generateImage()

    def generateImage(self): 
        self.image = Image.open(self.imgdir) # opening image
        self.draw_object = ImageDraw.Draw(self.image) # loafing draw module 
        
        # Adjust the position based on the number of digits
        if self.aqi >= 100:
            position = 100
        elif self.aqi >= 10:
            position = 130
        else:
            position = 150

        self.draw_object.text((position,100), toPersianNumerics(self.aqi), self.color, font=self.font) 
        
        # self.image.save("report.png")


        image_file = BytesIO()
        self.image.save(image_file, "PNG")
        image_file.seek(0)

        self.imageb = image_file
        return image_file

    def generateCaption(self):
        items = {"🔹شاخص آلودگی هوا : " : str(self.aqi),
                 "🔹وضعیت هوا : " : self.status_text,
                 "💧 رطوبت هوا : ": str(self.humidity),
                 "🌡 دمای هوا : ": str(self.temperature),
                 "🗓تاریخ : " : ' - '.join([x for x in today()]),
                 "🕓ساعت : " : now()
                }

        caption = [(item+items[item]) for item in items]
        caption = '\n'.join(x for x in caption)
        self.caption = toPersianNumerics(caption)
        
        return self.caption
