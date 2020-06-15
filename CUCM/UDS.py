import urllib3
import json
import requests
from pprint import pprint
import xmltodict
import xml.dom.minidom

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user = 'administrator'
pw = 'ciscopsdt'
host = '10.10.20.1'
path = 'cucm-uds/users'
url = f'https://{host}/{path}'

headers = {
    'Content-Type': 'application/xml',
    'Accept': 'application/xml'
}

response = requests.get(url, headers=headers, auth=(user, pw), verify=False)

tree = xml.dom.minidom.parseString(response.text)
pretty = tree.toprettyxml()
xmldata = xmltodict.parse(pretty)

users = xmldata['users']['user']
print(json.dumps(users, indent=2, sort_keys=True))
for user in users:
    print(f"{user['lastName']} {user['firstName']}")
    print(f" -{user['email']}")
    print(f"  -ID: {user['id']}")
    print()

