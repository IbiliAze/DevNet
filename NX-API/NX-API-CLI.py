import urllib3
import json
import requests
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


user = 'admin'
pw = 'Admin_1234!'
host = 'https://sbx-nxos-mgmt.cisco.com:443/ins'

headers = {
    'Content-Type': 'application/json'
}

payload = {
    'ins_api': {
        'version': '1.0',
        'type': 'cli_show',
        'chunk': '0',
        'sid': '1',
        'input': 'sh ip int br',
        'output_format': 'json'
    }
}

response = requests.post(host, headers=headers, data=json.dumps(payload), verify=False, auth=(user, pw)).json()
#Non-RESTful, everything has to be POSTed

print(json.dumps(response, indent=2, sort_keys=True))

