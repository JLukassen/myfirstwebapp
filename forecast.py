from datetime import datetime
from typing import List

from . import base

class DailyForecastItem(base.AutoInit):
     time: datetime
     temperature_high : float
     temperature_low : float
     summary: str = None
     precip_probability: float
     cloud_cover: float
     humidity: float
     wind_speed: float

class Forecast:
    daily: DailyForecast
    offset: int 

def __init__(
        self,
        latitude: float,
        longitude: float,
        daily: dict = None,
       
    ):
        self.latitude = latitude
        self.longitude = longitude      
        self.timezone = timezone
        self.daily = DailyForecast(timezone=timezone, **(daily or {}))
        self.offset = offset
      