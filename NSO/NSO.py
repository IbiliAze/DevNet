import requests
import json

url = 'http://localhost:8080/api'
auth = ('admin', 'admin')

headers = {'Accept': 'application/vnd.yang.collection+json'}

response = requests.get(f'{url}/running/devices/device', auth=auth, headers=headers).json()

devices = response['collection']['tailf-ncs:device']
for device in devices:
    print(f"Name: {device['name']}")
    print(f" -IP: {device['address']}")
    print(f"  -SSH Port: {device['port']}")
    print(f"   -Auth Group: {device['authgroup']}")
    print()
    
