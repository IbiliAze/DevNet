import json
from pprint import pprint
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user = 'ibi'
pw = 'cisco'
host = '10.1.1.1'
port = '443'
url = f"https://{host}:{port}/api/interfaces/physical"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

int_response = requests.get(url, headers=headers, auth = (user, pw), verify=False).json()

pprint(json.dumps(int_response, indent=2, sort_keys=True))