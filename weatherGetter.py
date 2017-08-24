import json
import urllib2

class WeatherGetter:
    """Gets current weather and forecast, will use
    forecast as current weather if offline."""

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.city = None
        self.country = None
        self._weather_api_key = ""
        print('WeatherGetter initialized')
        self.kelvin2c = -273.15

    def set_location(self, city=None, country=None, latitude=None, longitude=None):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

    def get_weather(self, city=None, country=None, latitude=None, longitude=None):
        city = city or self.city
        country = country or self.country
        latitude = latitude or self.latitude
        longitude = longitude or self.longitude

        if city and country:
            request = "http://api.openweathermap.org/data/2.5/weather?q"+ \
                      "=" + city + "," + country + \
                      "&appid=" + self._weather_api_key
        elif latitude and longitude:
            request = "http://api.openweathermap.org/data/2.5/weather?" + \
                      "lat=" + latitude + "&lon=" + longitude + \
                      "&appid=" + self._weather_api_key
        else:
            return

        data = json.load(urllib2.urlopen(request))

        print data['weather'][0]['description']

    def get_forecast(self, city=None, country=None, latitude=None, longitude=None):
        city = city or self.city
        country = country or self.country
        latitude = latitude or self.latitude
        longitude = longitude or self.longitude

        if city and country:
            request = "http://api.openweathermap.org/data/2.5/forecast?q" + \
                      "=" + city + "," + country + \
                      "&appid=" + self._weather_api_key
        elif latitude and longitude:
            request = "http://api.openweathermap.org/data/2.5/forecast?" + \
                      "lat=" + latitude + "&lon=" + longitude + \
                      "&appid=" + self._weather_api_key
        else:
            return

        data = json.load(urllib2.urlopen(request))

        print data['list']