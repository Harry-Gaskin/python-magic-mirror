import json
import urllib2

class LocationGetter:
    """Gets location from a source, also
    supports format conversion of location.
    Will store a sessions location formats locally"""

    def __init__(self):
        self._latitude = None
        self._longitude = None
        self._city = None
        self._country = None
        self._geocode_api_key = ""
        print('LocationGetter initialized')

    @property
    def latitude(self):
        if self._latitude:
            return self._latitude
        else:
            self._get_data()
            return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        if self._longitude:
            return self._longitude
        else:
            self._get_data()
            return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def city(self):
        if self._city:
            return self._city
        else:
            self._get_data()
            return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        if self._country:
            return self._country
        else:
            self._get_data()
            return self._country

    @country.setter
    def country(self, value):
        self._country = value

    def _get_data(self):

        if self._latitude and self._longitude:
            request = "https://maps.googleapis.com/maps/api/geocode/json?" + \
                      "latlng="+ self._latitude + "," + self._longitude + \
                      "&key=" + self._geocode_api_key

        elif self._city and self._country:
            request = "https://maps.googleapis.com/maps/api/geocode/json?" + \
                      "address=" + self._city + "," + self._country + \
                      "&key=" + self._geocode_api_key

        else:
            return

        data = json.load(urllib2.urlopen(request))

        if(data['status'] == "OK"):
            self._city = data['results'][0]['address_components'][3]['long_name']
            self._country = data['results'][0]['address_components'][5]['long_name']
            self._latitude = data['results'][0]['geometry']['location']['lat']
            self._longitude = data['results'][0]['geometry']['location']['lng']
