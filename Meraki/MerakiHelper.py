import requests
import json
from pprint import pprint
import urllib3
from requests.exceptions import HTTPError

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Meraki_Helper:

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Cisco-Meraki-API-Key': self.api_key
        }

    def req(self, method, endpoint, payload={}):
        url = f'https://api.meraki.com/api/v0/{endpoint}'
        headers = self.headers
        response = requests.request(method=method, url=url, 
            json=payload, headers=headers, verify=False)
        return response
