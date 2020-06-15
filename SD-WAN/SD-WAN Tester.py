import json
import requests
import urllib3
from requests.exceptions import HTTPError
from sdwansdk import SD_WAN_Helper


if __name__ == "__main__":

    sdwan_params_always_on = {
        'host': 'sandboxsdwan.cisco.com',
        'port': '8443',
        'username': 'devnetuser',
        'password': 'Cisco123!',
    }
    
    sdwan_params_reserved = {
        'host': '10.10.20.90',
        'port': '443',
        'username': 'admin',
        'password': 'admin',
    }

    # sdwan = SD_WAN_Helper(**sdwan_par
    

answer = 'woo'

print(1321) if answer == 'wojo' else print(2131212)