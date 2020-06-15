import jinja2
import json
import labenv
from pprint import pprint
from netmiko import ConnectHandler
import jinja2


devices_json = open("labenv.json", "r")
devices = json.load(devices_json)

config_file = '''
    interface Loopback 143
     ip address 13.32.12.32 255.255.255.0
     no shut
'''

for device in devices:
    with ConnectHandler(device['']) as connection:
        print ("G")



# devices_json = json.dumps(devices_dict)
# print(devices_json)