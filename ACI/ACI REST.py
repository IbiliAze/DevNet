import requests 
import json
from pprint import pprint
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'sandboxapicdc.cisco.com'
port = '443'
path = 'api/aaaLogin.json'
url = f"https://{host}:{port}/{path}"

payload = {
    "aaaUser":{
        "attributes":{
            "name": "admin",
            "pwd": "ciscopsdt"
        }
    }
}

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-Cookie'] = token

# print(json.dumps(response, indent=2, sort_keys=True))
# print(cookie['APIC-Cookie'])

path = 'api/node/mo/uni/tn-S2TBK/ap-AVOCADOS.json'
url = f"https://{host}:{port}/{path}"

response_get = requests.get(url, headers=headers, cookies=cookie, verify=False).json()
# print(url)
# # print(json.dumps(response_get, indent=2, sort_keys=True))

# payload_post = {
#     "fvAp": {
#         "attributes": {
#             "descr": "",
#             "dn": "uni/tn-S2TBK/ap-AVOCADOS"
#         }
#     }
# # }
# print(json.dumps(payload_post, indent=2, sort_keys=True))
# 

# response_post = requests.post(url, headers=headers, 
    # data=json.dumps(payload_post), cookies=cookie, verify=False).json()
# print(json.dumps(response_get, indent=2, sort_keys=True))