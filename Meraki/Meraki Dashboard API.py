from MerakiHelper import Meraki_Helper
import json

meraki = Meraki_Helper('c4b309558793850d92ce739fe2fd17a701295858')
org_id = "962199"
network_id = 'N_706502191543793968'
cameraId = 'N_706502191543794407'
wirelessId = 'N_706502191543794277'



''' get orgs '''
# response = meraki.req('GET', 'organizations').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get networks '''
# response = meraki.req('GET', f'organizations/{org_id}/networks').json()
# print(json.dumps(response, indent=2, sort_keys=True))
# for network in response:
#     print(network['name'])



''' delete networks '''
# response = meraki.req('DELETE', f'networks/N_706502191543794168')
# print(response)



''' post network '''
# payload = {
#     'name': 'Cameras2',
#     'type': 'camera'
# }
# response = meraki.req('POST', f'organizations/{org_id}/networks', payload=payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' post devices '''
# payload = {
#     "serial": "aaa",
# }
# response = meraki.req('POST', f'networks/{krk_network_id}/devices/claim').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' change device name '''
# payload = {
#     'name': 'AP 1'
# }
# response  = meraki.req(method='PUT', endpoint=f'networks/{krk_network_id}/devices/sn',
#     payload=payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get admins '''
# response = meraki.req('GET', f'organizations/{org_id}/admins').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get ssids '''
# response = meraki.req('GET', f'networks/{krk_network_id}/ssids').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get clients '''
# response = meraki.req('GET', f'networks/{krk_network_id}/clients').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get devices '''
# response = meraki.req('GET', f'networks/{krk_network_id}/devices').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get devices '''
# response = meraki.req('GET', f'networks/{krk_network_id}/devices').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get http servers '''
# response = meraki.req('GET', f'networks/{krk_network_id}/httpServers').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get servers '''
# response = meraki.req('GET', f'networks/{krk_network_id}/httpServers').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get networks'''
# response = meraki.req('GET', f'organizations/{org_id}/networks').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' delete networks'''
# response = meraki.req('DELETE', f'organizations/{org_id}/networks/N_706502191543794166')
# print(response)



''' create networks'''
# payload = {
#     'name': 'test',
#     'type': 'switch'
# }
# response = meraki.req('POST', f'organizations/{org_id}/networks', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' update networks'''
# payload = {
#     'name': 'test',
#     'type': 'camera switch'
# }
# response = meraki.req('PUT', f'networks/N_706502191543794256', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' post servers '''
# payload = {
#     'name': 'webhooks',
#     'url': 'https://testestes.com'
# }
# response = meraki.req('POST', f'networks/{network_id}/httpServers', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get servers'''
# response = meraki.req('GET', f'networks/{network_id}/httpServers').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' post test servers '''
# payload = {
#     'url': 'https://testestes.com'
# }
# response = meraki.req('POST', f'networks/{network_id}/httpServers/webhookTests', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get test server by id '''
# response = meraki.req('GET', f'networks/{network_id}/httpServers/webhookTests/706502191545371582').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' post wireless network '''
# payload = {
#     'name': 'Wireless Site',
#     'type': 'wireless'
# }
# response = meraki.req('POST', f'organizations/{org_id}/networks', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get ssid '''
# response = meraki.req('GET', f'networks/N_706502191543794277/ssids').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' put ssid xcap '''
# payload = {
#     '14':{
#         'ssid_body':{
#             'name': 'XCAP FREE WIFI',
#             'enabled': True,
#             'splashPage': 'Click-through splash page',
#             'authMode': 'open',
#             'walledGardenEnabled': False
#         },
#         'splash_body': 'null'
#     }
# }
# response = meraki.req('PUT', f'networks/N_706502191543794277/ssids/14', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get ssid '''
# response = meraki.req('GET', f'networks/{cameraId}/devices').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post wireless network '''
# payload = {
#     'name': 'Camera Site',
#     'type': 'camera'
# }b
# response = meraki.req('POST', f'organizations/{org_id}/networks', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get orgs '''
# response = meraki.req('GET', f'organizations').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' get nets '''
# response = meraki.req('GET', f'organizations/{org_id}/networks').json()
# print(json.dumps(response, indent=2, sort_keys=True))



''' post nets '''
# payload = {
#     'name': 'Test2',
#     'type': 'wireless switch'
# }
# response = meraki.req('POST', f'organizations/{org_id}/networks', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get clients '''
# response = meraki.req('GET', f'networks/{network_id}/devices').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get servers '''
# response = meraki.req('GET', f'networks/{network_id}/httpServers').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post servers '''
# paylaod = {
#     'url': 'https://www.test.com',
#     'name': 'test server'

# }
# response = meraki.req('delete', f'networks/{network_id}/httpServers', paylaod).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' delete servers '''
# response = meraki.req('delete', f'networks/{network_id}/httpServers/aHR0cHM6Ly93d3cudGVzdC5jb20=')
# print(response)).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get ssids '''
# response = meraki.req('GET', f'networks/{network_id}/ssids').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = meraki.req('GET', f'networks/{network_id}/devices/claims').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post admin '''
# payload = {
#     'name': 'jane doe',
#     'email': 'ibili74@gmail.com',
#     'orgAccess': 'full'
# }
# response = meraki.req('post', f'organizations/{org_id}/admins', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))





''' post network '''
# payload = {
#     'name': 'Test3',
#     'type': 'appliance'
# }
# response = meraki.req('post', f'organizations/{org_id}/networks', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))






''' post bind network template'''
# payload = {
#     'configTemplateId': 'Test3'
# }
# response = meraki.req('post', f'/networks/{network_id}/bind', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))






''' post combine networks'''
# payload = {
#     'name': 'Combined network',
#     'networkIds': [
#         'N_706502191543794407',
#         'N_706502191543794277'
#     ]
# }
# response = meraki.req('post', f'/organizations/{org_id}/networks/combine', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = meraki.req('GET', f'networks/{network_id}/httpServers').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post devices '''
# payload = {
#     'url': 'https://google.com',
#     'name': 'webhook'
# }
# response = meraki.req('post', f'networks/{network_id}/httpServers', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post networks '''
# response = meraki.req('get', f'organizations/{org_id}/networks').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post webhook logs '''
response = meraki.req('get', f'organizations/{org_id}/webhookLogs').json()
print(json.dumps(response, indent=2, sort_keys=True))




''' post networks '''
# payload = {
#     'name': 'Test5',
#     'type': 'camera'
# }
# response = meraki.req('post', f'organizations/{org_id}/networks', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))











