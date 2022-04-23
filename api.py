from abc import ABC, abstractmethod
from urllib.parse import urljoin
import requests

class IPAPI(ABC):
    @abstractmethod
    def completeLocation(self): ...
    @abstractmethod
    def specificLocationFied(self): ...

class SpecificIP(IPAPI):

    def completeLocation(self, ip):
        """
        HTTP Request
        GET `https://ipapi.co/{ip}/json/`
        """
        url = urljoin("https://ipapi.co", f"/{ip}/json/")
        response = requests.get(url)
        data = response.json()
        status_code = response.status_code
        latitude = str(data.get('latitude'))
        longitude = str(data.get('longitude'))
        map_loc = "https://www.google.com.ph/maps/@" + ",".join([latitude, longitude, "15z"])
        return data, map_loc, status_code

    def specificLocationFied(self, ip, field):
        """
        HTTP Request
        GET `https://ipapi.co/{ip}/{field}/`
        """
        url = urljoin("https://ipapi.co", f"{ip}/{field}")
        response = requests.get(url)
        return response.text, response.status_code

class ClientIP(IPAPI):

    def completeLocation(self):
        """
        HTTP Request
        GET `https://ipapi.co/json/`
        """
        url = urljoin("https://ipapi.co", "json")
        response = requests.get(url)
        return response.json(), response.status_code

    def specificLocationFied(self, field):
        """
        HTTP Request
        GET `https://ipapi.co/{field}/`
        """
        url = urljoin("https://ipapi.co", f"{field}")
        response = requests.get(url)
        return response.text, response.status_code

def getIPInfo(ip_address):
    base_url = "http://ip-api.com"
    url = urljoin(base_url, "json/{}".format(ip_address))
    response = requests.get(url)
    data = response.json()
    status_code = response.status_code
    latitude = str(data.get('lat'))
    longitude = str(data.get('lon'))
    map_loc = "https://www.google.com.ph/maps/@" + ",".join([latitude, longitude, "15z"])
    return data, map_loc, status_code
