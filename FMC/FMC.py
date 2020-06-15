import json
import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "https://fmcrestapisandbox.cisco.com"
login_url = '/api/fmc_platform/v1/auth/generatetoken'
url = f"{host}{login_url}"
headers = {
    'Content-Type': 'application/json'
}
user = 'ibili73'
pw = 'xra3wJ6U'

login_response = requests.post(
    url, auth=(user, pw), verify=False)

resp_headers = login_response.headers
token = resp_headers.get('X-auth-access-token', default=None)
headers['X-auth-access-token'] = token
# print(token)



path = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses'
url = f"{host}{path}"
apps = requests.get(url, headers=headers, verify=False).json()
# print(json.dumps(apps, indent=2, sort_keys=True))



path = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies'
url = f"{host}{path}"
policy_payload = {
  "type": "AccessPolicy",
  "name": "Sui Policy",
  "description": "yeah mi dawg",
  "defaultAction": {
    "intrusionPolicy": {
      "name": "yea man idk",
      "id": "id_of_existing_or_new_intrusion_policy", ########
      "type": "IntrusionPolicy"
    },
    "variableSet": {
      "name": "Default Set",
      "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
      "type": "VariableSet"
    },
    "type": "AccessPolicyDefaultAction",
    "logBegin": False,
    "logEnd": True,
    "sendEventsToFMC": True
  }
}

policy = requests.post(url, headers=headers, data=json.dumps(policy_payload), verify=False).json()
print("Created Policy")
print(json.dumps(policy, indent=2, sort_keys=True))
policyId = policy['id']


path = f'/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/{policyId}/accessrules'
url = f"{host}{path}"
rules_payload = {
  "sendEventsToFMC": True,
  "action": "ALLOW",
  "enabled": True,
  "type": "AccessRule",
  "name": "Malware Inspect",
  "logFiles": True,
  "logBegin": False,
  "logEnd": False,
  "variableSet": {
    "name": "Default Set",
    "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
    "type": "VariableSet"
  },
  "sourceNetworks": {
    "objects": [{
      "type": "NetworkGroup",
      "name": "IPv4-Private-All-RFC1918",
      "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f"
    }]
  },
  "filePolicy": {
    "name": "New Malware",
    "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
    "type": "FilePolicy"
  }
}
response = requests.post(url, headers=headers, data=json.dumps(rules_payload), verify=False).json()
print("Created the Rules")
print(json.dumps(response, indent=2, sort_keys=True))

path = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies'
url = f"{host}{path}"
delete_response = requests.delete(url, headers=headers, data=json.dumps(rules_payload), verify=False).json()
print(json.dumps(delete_response, indent=2, sort_keys=True))