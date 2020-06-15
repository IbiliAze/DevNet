import urllib3
import json
import requests
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user = 'admin'
pw = 'Admin_1234!'
host = 'sbx-nxos-mgmt.cisco.com'
port = '443'
headers = {
    'Content-Type': 'application/json',
}

payload = {
    "aaaUser":{
        "attributes":{
            "name": "admin",
            "pwd": "Admin_1234!"
        }
    }
}

login_url = f"https://{host}:{port}/api/mo/aaaLogin.json"
login_response = requests.post(login_url, headers=headers, json=(payload),
                              verify=False).json()
print(json.dumps(login_response, indent=2, sort_keys=True))

token = login_response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

paylaod = {
            "descr": "edited by a logit keyboard, do something about it"
        }

url = f"https://{host}:{port}/api/node/mo/sys/intf/phys-[eth1/90].json"

# response = requests.put(url, data=json.dumps(payload), headers=headers, cookies=cookie, verify=False).json()
# print(json.dumps(response, indent=2, sort_keys=True))

 