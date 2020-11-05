import json
import time
import urllib
import urllib2
import org.xml.sax.InputSource;
import simplejson
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
import webbrowser


class geoCodeAsync(BasedDarkSky):

HOST = 'https://maps.googleapis.com/maps/api/geocode/autocomplete/json'
maps_key = '&key=AIzaSyA0ddsSE8DUB0ZW0Fao9TXdvxvxYY8fYE4'


def __init__(self,maps_key: str, gzip: bool = True):
     super().__init__(map_key)
     self.request_manager = RequestMangerAsync(
            gzip=gzip
    )


def get_geocode(
        self,
        latitude: float,
        longitude: float,
        extend: bool = None,
        lang=languages.ENGLISH,
        values_units=units.AUTO,
        client_session: aiohttp.ClientSession = None
    )->Geocode:
         url = self.get_url(latitude, longitude)
        data = await self.request_manager.make_request(
            url=url,
            extend=weather.HOURLY if extend else None,
            lang=lang,
            units=values_units,
            exclude=exclude,
            client_session=client_session,
        )
        return Geocode(**data)


def my_view(request):
        if request.method = "POST":

def get_url(self, latitude: float, longitude: float, **params):
        if time is None:
            return "{host}/{map_key}/{latitude},{longitude}".format(
                map_key=self.map_key,
                host=self.HOST,
                latitude=latitude,
                longitude=longitude,
            )
        return "{host}/{api_key}/{latitude},{longitude}".format(
            map_key=self.map_key,
            host=self.HOST,
            latitude=latitude,
            longitude=longitude,
        
        )

  


filename = 'file:///home/yitakumini/Desktop/darkSky/index.html' 
webbrowser.open_new_tab(filename)