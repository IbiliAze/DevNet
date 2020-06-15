import requests 
import json
from pprint import pprint
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'sandboxapicdc.cisco.com'
port = '443'
path = 'api/aaaLogin.json'
url = f"https://{host}:{port}/{path}"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

payload = {
    "aaaUser":{
        "attributes":{
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}


response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-Cookie'] = token

# print(json.dumps(response, indent=2, sort_keys=True))
# print(cookie['APIC-Cookie'])

path = 'api/class/fvAp.json'
url = f"https://{host}:{port}/{path}"
response_get = requests.get(url, headers=headers, cookies=cookie, verify=False).json()
# print(url)
# print(json.dumps(response_get, indent=2, sort_keys=True))


path = 'api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json'
url = f"https://{host}:{port}/{path}"
response = requests.get(url, headers=headers, cookies=cookie, 
    verify=False).json()
# print(json.dumps(response, indent=2, sort_keys=True))


payload = {
    "fvAp": {
        "attributes": {
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet"
        }
    }
}
path = 'api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json'
url = f"https://{host}:{port}/{path}"
response = requests.post(url, headers=headers, cookies=cookie, data=json.dumps(payload),
    verify=False).json()
response = requests.get(url, headers=headers, cookies=cookie, 
    verify=False).json()
print(json.dumps(response, indent=2, sort_keys=True))
