import requests
import json
import urllib3
from requests.exceptions import HTTPError
from pprint import pprint

class DNA_Helper:

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password


    def token(self):
        ''' get the token '''
        try:
            path = 'dna/system/api/v1/auth/token'
            url = f"https://{self.host}/{path}"
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            auth = (self.username, self.password)
            response = requests.post(url, headers=headers, auth=(auth), verify = False).json()
            token = response['Token']
            # print(json.dumps(response, indent=2, sort_keys=True))
            headers['X-Auth-Token'] = token
            return headers
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)

    def req(self, method, endpoint, payload={}):
        response = requests.request(method=method, url=f'https://{self.host}/dna/intent/api/v1{endpoint}', headers=self.token(), json=payload, verify=False)
        return response