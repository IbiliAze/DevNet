import requests 
import json
from pprint import pprint
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user = 'developer'
pw = 'C1sco12345'
host = 'ios-xe-mgmt-latest.cisco.com'
port = '9443'
path = 'restconf/data/ietf-interfaces:interfaces'
url = f"https://{host}:{port}/{path}"

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

response = requests.get(url, headers=headers,
    auth=(user, pw), verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))

payload  = {
    "interface": {
        "description": "edited by a logi keyboard do something about it",
        "enabled": True,
        "ietf-ip:ipv4": {},
        "ietf-ip:ipv6": {},
        "name": "Loopback1999",
        "type": "iana-if-type:softwareLoopback"
    }
}

##### Creating a Loopback1999 Interface
path = 'restconf/data/ietf-interfaces:interfaces'
url = f"https://{host}:{port}/{path}"
loopback1999 = requests.post(url, headers=headers,
    data=json.dumps(payload), auth=(user, pw), verify=False).json()
print(json.dumps(loopback1999, indent=2, sort_keys=True))


##### Deleting the Loopback1999 Interface
payload  = {
    "interface": {
        "description": "",
        "enabled": False,
        "ietf-ip:ipv4": {},
        "ietf-ip:ipv6": {},
        "name": "Loopback1999",
        "type": "iana-if-type:softwareLoopback"
    }
}
path = 'restconf/data/ietf-interfaces:interfaces/interface=Loopback1999'
url = f"https://{host}:{port}/{path}"
deleting_loopback1999 = requests.delete(url, headers=headers, 
    auth=(user, pw), verify=False).json()
print(json.dumps(response, indent=2, sort_keys=True))