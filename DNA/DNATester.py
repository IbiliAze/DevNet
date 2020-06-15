import requests
import json
from pprint import pprint
import urllib3
from requests.exceptions import HTTPError
from DNAHelper import DNA_Helper

dna_params_always_on = {
    'host': 'sandboxdnac2.cisco.com',
    'username': 'devnetuser',
    'password': 'Cisco123!',
}

dcloud_params = {
    'host': 'dcloud-dna-center-inst-rtp.cisco.com',
    'username': 'demo',
    'password': 'demo1234!',
}

dna = DNA_Helper(**dna_params_always_on)





''' get sites '''
# response = dna.req('GET', '/site').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = dna.req('GET', '/site/devices').json()
# print(json.dumps(response, indent=2, sort_keys=True))
# response = dna.req('GET', '/network-device').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get site topology '''
# response = dna.req('GET', '/topology/site-topology').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = dna.req('GET', '/network-device').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = dna.req('GET', '/client-health?timestamp=').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = dna.req('GET', '/client-health?timestamp=').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get cli creds '''
# response = dna.req('GET', '/global-credential?credentialSubType=CLI').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get snmp creds '''
# response = dna.req('GET', '/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get events '''
# response = dna.req('GET', '/events?tags=ASSURANCE').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get cli creds '''
# response = dna.req('GET', '/global-credential?credentialSubType').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get task '''
# response = dna.req('GET', '/task/hgfgfh').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get creds '''
# response = dna.req('GET', '/global-credential?credentialSubType=CLI').json()
# cli_cred = response['response'][0]['id']
# response = dna.req('GET', '/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY').json()
# snmp_cred = response['response'][0]['id']
# print(json.dumps(response, indent=2, sort_keys=True))




''' post discovery '''
# payload = {
#     'name': 'disc',
#     'discoveryType': 'Range',
#     'ipAddressList': '10.0.0.0-10.255.255.254',
#     'protocolOrder': 'ssh, telnet',
#     'preferredMgmtIpMethod': 'None',
#     'globalCredentialList' :[cli_cred, snmp_cred]
# }
# response = dna.req('POST', '/discovery', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post commnd runner '''
# payload = {
#     'name': 'disc',
#     'discoveryType': 'Range',
#     'ipAddressList': '10.0.0.0-10.255.255.254',
#     'protocolOrder': 'ssh, telnet',
#     'preferredMgmtIpMethod': 'None'
# }
# response = dna.req('POST', '/network-device-poller/cli/read-request', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get events '''
# response = dna.req('GET', '/events?tags=ASSURANCE').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post command runer'''
# payload = {
#     'commands': ['disc'],
#     'deviceUuids': ['Range']
# }
# response = dna.req('POST', '/network-device-poller/cli/read-request', payload).json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get health '''
# healths = ['site', 'client', 'network']
# for health in healths: 
#     response = dna.req('GET', f'/{health}-health?timestamp=').json()
#     print(json.dumps(response, indent=2, sort_keys=True))




''' get events '''
# response = dna.req('GET', '/events?tags=ASSURANCE').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get event count '''
# response = dna.req('GET', '/events/count?tags=ASSURANCE').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get event subscriptions '''
# response = dna.req('GET', '/event/subscription').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get event notifications '''
# response = dna.req('GET', '/event/event-series').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get event notification count '''
# response = dna.req('GET', '/event/event-series/count').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get sites '''
# response = dna.req('GET', '/site').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get topology '''
# response = dna.req('GET', '/topology/site-topology').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get site count '''
# response = dna.req('GET', '/site/count').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get site device memberships '''
# response = dna.req('GET', '/membership/').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get vlans '''
# response = dna.req('GET', '/topology/vlan/vlan-names').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' post command runner '''
# payload = {
#     'commands': ['sh ver', 'sh process'],
#     'deviceUuids': ['deviceid']
# }
# response = dna.req('POST', '/network-device-poller/cli/read-request').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get accepted commands '''
# response = dna.req('GET', '/network-device-poller/cli/legit-reads').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get creds '''
# response = dna.req('GET', '/global-credential?credentialSubType=CLI').json()
# response = dna.req('GET', '/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY').json()
# response = dna.req('GET', '/global-credential?credentialSubType=SNMPV2_READ_COMMUNITY').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get devices '''
# response = dna.req('GET', '/network-device').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get device health '''
# response = dna.req('GET', '/device-health?timestamp=').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get events '''
# response = dna.req('GET', '/events?tags=ASSURANCE').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get creds '''
# response = dna.req('GET', '/global-credential?credentialSubType=SNMPV2_READ_COMMUNITY').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get runnable commands '''
# response = dna.req('GET', '/network-device-poller/cli/legit-reads').json()
# print(json.dumps(response, indent=2, sort_keys=True))




''' get site count '''
# response = dna.req('GET', '/site/count').json()
# print(json.dumps(response, indent=2, sort_keys=True))









