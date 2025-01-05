from flask import send_file
from functions.date.date_calculator import DateCalculator
from image.date.date_image_creator import DateImageCreator

class DateImageAPI:
    def __init__(self):
        self.calculator = DateCalculator()
        self.creator = DateImageCreator()

    def get_date_image(self):
        date_data = {
            'solar': self.calculator.get_solar_date(),
            'lunar': self.calculator.get_lunar_date(),
            'ganzhi': self.calculator.get_ganzhi_date(),
            'season': self.calculator.get_season_info(),
            'festival': self.calculator.get_festival_info()
        }
        
        img = self.creator.create_date_image(date_data)
        img_io = self.creator.get_image_bytes(img)
        
        return send_file(img_io, mimetype='image/jpeg') 