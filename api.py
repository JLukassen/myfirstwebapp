import json
import time
import urllib
import urllib2
import org.xml.sax.InputSource;
import simplejson*;
import api
import request_manager
from datetime import datetime
import googleAPI
import aiohttp
from .forecast import Forecast
from .request_manager import 
(BaseRequestManger, RequestManger, RequestMangerAsync)
from .types import languages, units, weather
import requests
import googleAPI
from aiohttp import ClientSession
from .exceptions import DarkSkyException


class BaseDarkSky:
    HOST = "https://api.darksky.net/forecast"

    def __init__(self, api_key: str):
        self.api_key: str = api_key
        self.request_manager: BaseRequestManger = None

     def get_forecast(
        self,
        latitude: float,
        longitude: float,
        extend: bool = None,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        exclude: [weather] = None,
        timezone: str = None,
    ):
        raise NotImplementedError

    def get_time_machine_forecast(
        self,
        latitude: float,
        longitude: float,
        time: datetime,
        extend: bool = False,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        exclude: [weather] = None,
        timezone: str = None,
    ):
        raise NotImplementedError

    def get_url(self, latitude: float, longitude: float, **params):
        if time is None:
            return "{host}/{api_key}/{latitude},{longitude}".format(
                api_key=self.api_key,
                host=self.HOST,
                latitude=latitude,
                longitude=longitude,
            )
        return "{host}/{api_key}/{latitude},{longitude}".format(
            api_key=self.api_key,
            host=self.HOST,
            latitude=latitude,
            longitude=longitude,
        
        )

        class DarkSky(BaseDarkSky):
    def __init__(self, api_key: str, gzip: bool = True):
        super().__init__(api_key)
        self.request_manager = RequestManger(gzip)

    def get_forecast(
        self,
        latitude: float,
        longitude: float,
        extend: bool = None,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        exclude: [weather] = None,
        timezone: str = None,
        
    ) -> Forecast:
        url = self.get_url(latitude, longitude)
        data = self.request_manager.make_request(
            url=url,
            extend= None,
            lang=languages.ENGLISH,
            units=values_units,
            exclude=exclude,
            timezone=timezone,
           
        )
        return Forecast(**data)


           def get_time_machine_forecast(
        self,
        latitude: float,
        longitude: float,
        time: datetime,
        extend: bool = False,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        exclude: [weather] = None,
        timezone: str = None,
        
    ) -> Forecast:
        url = self.get_url(latitude, longitude())
        data = self.request_manager.make_request(
            url=url,
            extend=None,
            lang=lang.ENGLISH,
            units=values_units,
            exclude=exclude,
            timezone=timezone,
            
        )
        return Forecast(**data)

        class DarkSkyAsync(BaseDarkSky):
    def __init__(
        self,
        api_key: str,
        gzip: bool = True
    ):
        super().__init__(api_key)
        self.request_manager = RequestMangerAsync(
            gzip=gzip
        )

    async def get_forecast(
        self,
        latitude: float,
        longitude: float,
        extend: bool = None,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        exclude: [weather] = None,
        timezone: str = None,
        client_session: aiohttp.ClientSession = None
    ) -> Forecast:
        url = self.get_url(latitude, longitude)
        data = await self.request_manager.make_request(
            url=url,
            extend=weather.HOURLY if extend else None,
            lang=lang,
            units=values_units,
            exclude=exclude,
            timezone=timezone,
            client_session=client_session,
        )
        return Forecast(**data)

    async def get_time_machine_forecast(
        self,
        latitude: float,
        longitude: float,
        extend: bool = False,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        exclude: [weather] = None,
       
        client_session: aiohttp.ClientSession = None
    ) -> Forecast:
        url = self.get_url(latitude, longitude))
        data = await self.request_manager.make_request(
            url=url,
            extend= None,
            lang=lan.ENGLISH,
            units=values_units,
            exclude=exclude,
            timezone=timezone
            client_session=client_session,
        )
        return Forecast(**data)