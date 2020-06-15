from dnacentersdk import api
import time
import calendar
import json
from pprint import pprint

dna = api.DNACenterAPI(base_url='https://sandboxdnac2.cisco.com',
                       username='devnetuser', password='Cisco123!')

sites = dna.networks.get_site_topology()
print(json.dumps(sites, indent=2, sort_keys=True))

for site in sites.response.sites:
    if site.parentId == 'e95d9cef-2a00-4eb9-82df-01c3291410be':
        print(site.name)
        for child_sites in sites.response.sites:
            if child_sites.parentId == site.id:
                print(f"    {child_sites.name}")
            for more_children in sites.response.sites:
                if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                    print(f"    {more_children.name}")
    print()


vlans = dna.networks.get_vlan_details()
for vlan in vlans.response:
    print(vlan)


devices = dna.devices.get_device_list()
print(json.dumps(devices, indent=2, sort_keys=True))
for device in devices.response:
    print(device.family)
    print(" ", device.platformId)
    print("  ", device.series)
    print("   ", device.type)
    print("     ", device.softwaretype)
    print("      ", device.id)
    print()

device = dna.devices.get_device_by_id('bafa2b45-b827-48d5-9022-8c66b5a5b18f')
print(json.dumps(device, indent=2, sort_keys=True))

epoch = calendar.timegm(time.gmtime())
# clients = dna.clients.get_overall_client_health(timestamp=str(epoch))
clients = dna.clients.get_overall_client_health()
print(json.dumps(clients, indent=2, sort_keys=True))
