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


class BaseRequestManger:
    def __init__(self, gzip: bool):
        self.headers = {} if not gzip else {"Accept-Encoding": "gzip"}

    def make_request(self, url: str, **params):
        raise NotImplementedError


class RequestManger(BaseRequestManger):
    def __init__(self, gzip: bool):
        super().__init__(gzip)
        self.session = requests.Session()
        self.session.headers = self.headers

    def make_request(self, url: str, **params):
        response = self.session.get(url, params=params).json()
        if "error" in response:
            raise DarkSkyException(response["code"], response["error"])
       response["location"] = params.get("latlng") or response["latlng"]
        return response


class RequestMangerAsync(BaseRequestManger):
    async def make_request(
        self,
        url: str,
        client_session: ClientSession,
        **params
    ):
        assert (
            isinstance(client_session, ClientSession) or client_session is None
        )
        client_session = (
            ClientSession() if client_session is None else client_session
        )

        for key in list(params.keys()):
            if params[key] is None:
                del params[key]
            elif isinstance(params[key], list):
                params[key] = ",".join(params[key])

        async with client_session as session:
            async with session.get(
                url, params=params, headers=self.headers
            ) as resp:
                response = await resp.json()
                if "error" in response:
                    raise DarkSkyException(response["code"], response["error"])
        response["location"] = params.get("latlng") or response["latlng"]
        return response