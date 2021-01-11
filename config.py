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
import json
import os
class Config:
    def __init__(self, file_path = None, ):
        if not file_path:
            self.file_path = 'config.conf.json'
        else:
            self.file_path = file_path
        self._read()

    def _read(self):
        with open(self.file_path, 'r') as file:
            self._config = json.load(file)
        
        for key, value in self._config.items():
            setattr(self, key, value)

class MeasureTracker(Config):
    
    def __init__(self, file_path="last_measure.conf.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            self.setMeasure(-1)
        
        super().__init__(self.file_path)

    def setMeasure(self, measure: int):
        with open(self.file_path, 'w+') as file:
            json.dump({'last_measure': measure}, file)
