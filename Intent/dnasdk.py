import requests
import json
import urllib3
from requests.exceptions import HTTPError
from pprint import pprint

class DNA:

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self, host, username, password):

        self.host = host
        self.username = username
        self.password = password

        ''' get the token '''
        try:
            path = 'dna/system/api/v1/auth/token'
            url = f"https://{self.host}/{path}"
            self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            auth = (self.username, self.password)
            response = requests.post(url, headers=self.headers, auth=(auth), verify = False).json()
            self.token = response['Token']
            self.headers['X-Auth-Token'] = self.token
            # print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def req(self, method, endpoint, payload={}):
        ''' request helper function '''
        response = requests.request(method=method, url=f'https://{self.host}/dna{endpoint}', 
            headers=self.headers, json=payload)
        return response



    ''' Sites '''

    def get_sites(self):
        ''' get sites '''
        try:
            endpoint = '/intent/api/v1/site'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_site_health(self, query='?timestamp='):
        ''' get site health'''
        try:
            endpoint = f'/intent/api/v1/site-health{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_site_count(self, query=''):
        ''' get site count '''
        try:
            endpoint = f'/intent/api/v1/site/count{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_site_memberships(self, site_id):
        ''' get site and device memberships '''
        try:
            endpoint = f'/intent/api/v1/membership/{site_id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_site(self, type='', site_name='', parent_name_for_site='', building_name='',
        building_address='', parent_name_for_building='', building_latitude=0, building_longtitute=0, floor_name='',
        parent_name_for_floor = '', floor_rf_model='', floor_width=0, floor_length=0, floor_height=0, delete=False):
        ''' create a site '''
        try:
            if delete == False:
                payload = {
                    "type": type,
                    "site": {
                        "area": {
                            "name": site_name,
                            "parentName": parent_name_for_site
                        },
                        "building": {
                            "name": building_name,
                            "address": building_address,
                            "parentName": parent_name_for_building,
                            "latitude": building_latitude,
                            "longitude": building_longtitute
                        },
                        "floor": {
                            "name": floor_name,
                            "parentName": parent_name_for_floor,
                            "rfModel": floor_rf_model,
                            "width": floor_width,
                            "length": floor_length,
                            "height": floor_height
                        }
                    }
                }
                endpoint = f'/intent/api/v1/site'
                response = self.req('post', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                site_id = str(input('Enter the Site ID'))
                endpoint = f'/intent/api/v1/site/{site_id}'
                response = self.req('delete', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            return response

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_assign_device_to_site(self, site_id, *device_ip):
        ''' assign devices to a site '''
        try:
            payload = {
                "device": [
                    {
                      "ip": list(device_ip)
                    }
                ]
            }
            endpoint = f'/intent/api/v1/site/{site_id}/device'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Topology '''

    def get_site_topolgy(self, query=''):
        ''' get site topolgies '''
        try:
            endpoint = f'/intent/api/v1/topology/site-topology{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_physical_topology(self, query=''):
        ''' get physical topolgies '''
        try:
            endpoint = f'/intent/api/v1/topology/physical-topology{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_vlans(self, query=''):
        ''' get vlans '''
        try:
            endpoint = f'/intent/api/v1/topology/vlan/vlan-names{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Networks '''

    def get_network(self, query=''):
        ''' get networks '''
        try:
            endpoint = f'/intent/api/v1/network{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_network(self):
        ''' create a network for dhcp and dns center server settings '''


    def get_service_provider(self, query=''):
        ''' get service provider details '''
        try:
            endpoint = f'/intent/api/v1/service-provider{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_service_provider_profile(self, name, model='', wan_provider='', delete=False):
        ''' create a service provider profile (qos) '''
        try:
            if delete == False:
                payload = {
                    "settings": {
                        "qos": [
                            {
                                "profileName": name,
                                "model": model,
                                "wanProvider": wan_provider
                            }
                        ]
                    }
                }
                endpoint = f'/intent/api/v1/service-provider'
                response = self.req('post', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/intent/api/v1/service-provider/{name}'
                response = self.req('delete', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            return response

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_global_pool(self, query=''):
        ''' get the global pool details such as dhcp, dns, default gateways'''
        try:
            endpoint = f'/intent/api/v1/global-pool{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_global_pool(self, name='', cird='', gateway='', dns_ips='', dhcp_ips='', ipv4_or_ipv6='', type='Generic', delete=False):
        ''' create a global pool '''
        try:
            if delete == False:
                payload = {
                    "settings": {
                        "ippool": [
                            {
                                "ipPoolName": name,
                                "type": type,
                                "ipPoolCidr": cird,
                                "gateway": gateway,
                                "dhcpServerIps": dhcp_ips,
                                "dnsServerIps": dns_ips,
                                "IpAddressSpace": ipv4_or_ipv6
                            }
                        ]
                    }
                }
                endpoint = f'/intent/api/v1/global-pool'
                response = self.req('post', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                pool_id = str(input('Enter the Pool ID'))
                endpoint = f'/intent/api/v1/global-pool/{pool_id}'
                response = self.req('post', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            return response

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_health(self, query='?timestamp='):
        ''' get network health '''
        try:
            endpoint = f'/intent/api/v1/network-health{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Devices and Interfaces '''

    def get_devices(self, id='', query=''):
        ''' get devices '''
        try:
            if id == '':
                endpoint = f'/intent/api/v1/network-device{query}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/intent/api/v1/network-device/{id}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_information_brief(self, id):
        ''' get device information bried '''
        try:
            endpoint = f'/intent/api/v1/network-device/{id}/brief'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_count(self):
        ''' get device count '''
        try:
            endpoint = f'/intent/api/v1/network-device/count'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_ospf_interfaces(self):
        ''' get device ospf interfaces '''
        try:
            endpoint = f'/intent/api/v1/interface/ospf'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_config(self, id='', query=''):
        ''' get device configs '''
        try:
            if id == '':
                endpoint = f'/intent/api/v1/network-device/config'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/intent/api/v1/network-device/{id}/config'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))

            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_interfaces(self, query=''):
        ''' get all interfaces '''
        try:
            endpoint = f'/intent/api/v1/interface'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_interface_count(self, query=''):
        ''' get interface count '''
        try:
            endpoint = f'/intent/api/v1/interface/count'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_interface_by_ip(self, ip_address):
        ''' get interface details by an ip address '''
        try:
            endpoint = f'/intent/api/v1/interface/ip-address/{ip_address}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_interface_by_id(self, id):
        ''' get interface details by id '''
        try:
            endpoint = f'/intent/api/v1/interface/{id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_details(self, query=''):
        ''' get all interfaces '''
        try:
            endpoint = f'/intent/api/v1/device-detail'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_functional_capability(self, query=''):
        ''' get device functional capability '''
        try:
            endpoint = f'/intent/api/v1/network-device/functional-capability'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_module_by_id(self, id):
        ''' get interface details by id '''
        try:
            endpoint = f'/intent/api/v1/network-device/module/{id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_device(self):
        ''' add a new network device '''
        try:
            payload = {
                "cliTransport": "string",
                "computeDevice": True,
                "enablePassword": "string",
                "extendedDiscoveryInfo": "string",
                "httpPassword": "string",
                "httpPort": "string",
                "httpSecure": True,
                "httpUserName": "string",
                "ipAddress": [
                  "string"
                ],
                "merakiOrgId": [
                  "string"
                ],
                "netconfPort": "string",
                "password": "string",
                "serialNumber": "string",
                "snmpAuthPassphrase": "string",
                "snmpAuthProtocol": "string",
                "snmpMode": "string",
                "snmpPrivPassphrase": "string",
                "snmpPrivProtocol": "string",
                "snmpROCommunity": "string",
                "snmpRWCommunity": "string",
                "snmpRetry": 0,
                "snmpTimeout": 0,
                "snmpUserName": "string",
                "snmpVersion": "string",
                "type": "COMPUTE_DEVICE",
                "updateMgmtIPaddressList": [
                  {
                    "existMgmtIpAddress": "string",
                    "newMgmtIpAddress": "string"
                  }
                ],
                "userName": "string"
            }
            endpoint = f'/intent/api/v1/network-device'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Clients '''

    def get_client_health(self, query='?timestamp='):
        ''' get client health '''
        try:
            endpoint = f'/intent/api/v1/client-health{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_detail(self, query='?timestamp=&macAddress='):
        ''' get client details by mac address '''
        try:
            endpoint = f'/intent/api/v1/client-detail{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Command Runner API '''

    def get_command_runner_legit_reads(self):
        ''' get a list of legit commands to run with the command runner api '''
        try:
            endpoint = f'/intent/api/v1/network-device-poller/cli/legit-reads'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_command_runner(self, command, name='show commands', timeout=0, *device_Uuids_list):
        ''' command runner api '''
        try:
            payload = {
                "commands": command,
                "description": f'{name} description',
                "deviceUuids": list(device_Uuids_list),
                "name": name,
                "timeout": timeout
            }
            endpoint = f'/intent/api/v1/network-device-poller/cli/read-request'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Credentials '''

    def get_credentials_cli(self):
        ''' get credentials of each device for discovery '''
        try:
            endpoint = f'/intent/api/v1/global-credential?credentialSubType=CLI'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_credentials_snmp(self):
        ''' get SNMP credentials of each device for discovery '''
        try:
            endpoint = f'/intent/api/v1/global-credential?credentialSubType=SNMPV2_READ_REQUEST'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_device_cli_credentials(self, username, password, enable_password, description=''):
        ''' create device cli credentials '''
        try:
            payload = {
                "settings": {
                    "cliCredential": [
                        {
                          "description": description,
                          "username": username,
                          "password": password,
                          "enablePassword": enable_password
                        }
                    ]
                }
            }
            endpoint = f'/intent/api/v1/device-credential'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_device_snmp_credentials(self, username, password, description, community_string, auth_password, key, encryption='AES128', auth_type='SHA'):
        ''' create snmpv3 read/write community strings '''
        try:
            payload = {
                'settings': {
                    "snmpV2cRead": [
                        {
                            "description": description,
                            "readCommunity": community_string
                        }
                    ],
                    "snmpV2cWrite": [
                        {
                            "description": description,
                            "writeCommunity": community_string
                        }
                    ],
                    "snmpV3": [
                        {
                            "description": description,
                            "username": username,
                            "privacyType": encryption,
                            "privacyPassword": key,
                            "authType": auth_type,
                            "authPassword": auth_password,
                            "snmpMode": "AUTHPRIV"
                        }
                    ]
                }
            }
            endpoint = f'/intent/api/v1/device-credential'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_device_http_credentials(self, name, username, password, port):
        ''' create http read/write credentials '''
        try:
            payload = {
                'settings':{
                    "httpsRead": [
                        {
                            "name": name,
                            "username": username,
                            "password": password,
                            "port": port
                        }
                        ],
                    "httpsWrite": [
                        {
                            "name": name,
                            "username": username,
                            "password": password,
                            "port": port
                        }
                    ]
                }
            }
            endpoint = f'/intent/api/v1/device-credential'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_assign_credential_to_site(self, site_id, cliId='', snmpv2R_id='', snmpv2W_id='', snmpv3_id='', httpR_id='', httpW_id=''):
        ''' assign credentials to site '''
        try:
            payload = {
                "cliId": cliId,
                "snmpV2ReadId": snmpv2R_id,
                "snmpV2WriteId": snmpv2W_id,
                "httpRead": httpR_id,
                "httpWrite": httpW_id,
                "snmpV3Id": snmpv3_id
            }
            endpoint = f'/intent/api/v1/credential-to-site/{site_id}'
            response = self.req('post', endpoint, payload=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Device Discovery '''

    def post_device_discovery(self, name, ip_range, timeout):
        ''' discover devices '''
        try:
            cli_read = self.get_credentials_cli()['response'][0]['id']
            snmp_read = self.get_credentials_snmp()['response'][0]['id']
            payload = {
                'name': name,
                'discoveryType': 'Range',
                'ipAddressList': ip_range,
                'timeout' : timeout,
                'protocolOrder' : 'ssh,telnet',
                'preferredMgmtIpMethod': 'None',
                'globalCredentialList': [cli_read, snmp_read]
            }
            endpoint = '/intent/api/v1/discovery'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovery_count(self):
        ''' get discovery count '''
        try:
            endpoint = f'/intent/api/v1/discovery/count'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovery_by_range(self, start_index, records_to_return):
        ''' get discovery id '''
        try:
            endpoint = f'/intent/api/v1/discovery/{start_index}/{records_to_return}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovery_summary(self, discovery_id, query=''):
        ''' get discovered devices '''
        try:
            endpoint = f'/intent/api/v1/discovery/{id}/summary'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovery_by_id(self, discovey_id):
        ''' get discovery details by discovery id '''
        try:
            endpoint = f'/intent/api/v1/discovery/{id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovery_list(self, discovery_id, query=''):
        ''' get discoveries '''
        try:
            endpoint = f'/intent/api/v1/discovery/{id}/job'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovered_devices(self, discovery_id, query=''):
        ''' get discovered network devices '''
        try:
            endpoint = f'/intent/api/v1/discovery/{id}/network-device'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovered_device_count(self, discovery_id):
        ''' get discovered network devices count '''
        try:
            endpoint = f'/intent/api/v1/discovery/{id}/network-device/count'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_discovery_jobs_by_ip(self, ip, query=''):
        ''' get list of discovery jobs by a given ip '''
        try:
            endpoint = f'/intent/api/v1/discovery/job?ipAddress={ip}&{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Path Trace '''

    def post_path_trace(self, dest_ip='', dest_port='', protocol='', source_ip='', source_port='', periodic_refresh=True,
        delete=False):
        ''' path trace api '''
        try:
            if delete == False:
                payload = {
                    "controlPath": True,
                    "destIP": dest_ip,
                    "destPort": dest_port,
                    "inclusions": [
                        "string"
                    ],
                    "periodicRefresh": periodic_refresh,
                    "protocol": protocol,
                    "sourceIP": source_ip,
                    "sourcePort": source_port
                }
                endpoint = f'/intent/api/v1/flow-analysis'
                response = self.req('post', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                flow_id = str(input('Enter the Flow-Analysis ID'))
                endpoint = f'/intent/api/v1/global-pool/{flow_id}'
                response = self.req('delete', endpoint, payload=payload).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            return response

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_flow_analysis(self, query=''):
        try:
            endpoint = f'/intent/api/v1/flow-analysis{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Assurance '''

    def get_event_assurance(self):
        try:
            endpoint = f'/intent/api/v1/events?tags=ASSURANCE'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_event_count(self):
        ''' get event count '''
        try:
            endpoint = f'/intent/api/v1/events/count?tags=ASSURANCE'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_event_subscription(self, url, subscription_name, subscription_description, put_or_post, *events):
        ''' subscribe to an event '''
        try:
            payload = [
                {
                    'name': subscription_name,
                    'subscriptionEndpoints': [
                        {
                            'subscriptionDetails': {
                                'connectorType': 'REST',
                                'name': f'{subscription_name} App',
                                'description': subscription_description,
                                'method': put_or_post,
                                'url': url
                            }
                        }
                    ],
                    'filter': {
                        'eventIds': list(events)
                    }
                }
            ]
            endpoint = '/intent/api/v1/event/subscription'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_event_subscriptions(self, query=''):
        ''' get event subscriptions '''
        try:
            endpoint = f'/intent/api/v1/event/subscription'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_subscription_count(self, query=''):
        ''' get event subscription count '''
        try:
            endpoint = f'/intent/api/v1/event/subscription/count'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_event_notification(self, query=''):
        ''' get event notifications '''
        try:
            endpoint = f'/intent/api/v1/event/event-series'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_event_notification_count(self, query=''):
        ''' get event notifications count '''
        try:
            endpoint = f'/intent/api/v1/event/event-series/count'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Templates '''

    def get_templates(self, template_id='', query=''):
        ''' get available config templates '''
        try:
            if template_id == '':
                endpoint = f'/intent/api/v1/template-programmer/template{query}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
                return response
            else:
                endpoint = f'/intent/api/v1/template-programmer/template/{template_id}{query}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
                return response

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
            

    def get_projects(self, query=''):
        ''' get projects '''
        try:
            endpoint = f'/intent/api/v1/template-programmer/project{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
            

    def post_projects(self, name, description=''):
        ''' create projects '''
        try:
            payload = {
                'name': name,
                'description': description
            }
            endpoint = f'/intent/api/v1/template-programmer/project'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_templates(self, project_id, name, device_family, device_series, software_type, composite=False):
        ''' create templates '''
        try:
            payload = {
                'name': name,
                'composite': composite,
                'deviceTypes': [
                    {
                        'productFamily': device_family,
                        'productSeries': device_series
                    }
                ],
                'softwareType': software_type
            }
            endpoint = f'/intent/api/v1/template-programmer/project/{project_id}/template'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def put_template_preview(self, template_id, params):
        ''' render the template with data '''
        try:
            payload = {
                'params': params,
                'templateId': template_id
            }
            endpoint = f'/intent/api/v1/template-programmer/template/preview'
            response = self.req('put', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_version_templates(self, template_id, comments=''):
        ''' version a template before deployment '''
        try:
            payload = {
                'comments': comments,
                'templateId': template_id
            }
            endpoint = f'/intent/api/v1/template-programmer/template/version'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_deploy_templates(self, template_id, params, type, *ip_addresses):
        ''' deploy a template '''
        try:
            payload = {
                'forcePushTemplate': False,
                'targetInfo': [
                    {
                        'id': ip_addresses,
                        'params': params,
                        'type': type
                    }
                ],
                'templateId': template_id
            }
            endpoint = f'/intent/api/v1/template-programmer/template/deploy'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_template_deployment_status(self, template_id):
        ''' get the status of the deployed template '''
        try:
            endpoint = f'/intent/api/v1/template-programmer/template/deploy/{template_id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Enrichment Details '''

    def get_client_enrichment_details(self, query=''):
        ''' get client enrichment details '''
        try:
            endpoint = f'/intent/api/v1/client-enrichment-details{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_user_enrichment_details(self, query=''):
        ''' get user enrichment details '''
        try:
            endpoint = f'/intent/api/v1/user-enrichment-details{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_issue_enrichment_details(self, query=''):
        ''' get network issues enrichment details '''
        try:
            endpoint = f'/intent/api/v1/issue-enrichment-details'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_enrichment_details(self, query=''):
        ''' get device enrichment details '''
        try:
            endpoint = f'/intent/api/v1/device-enrichment-details{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Task '''

    def get_task_count(self, query=''):
        ''' get task count '''
        try:
            endpoint = f'/intent/api/v1/task/count{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)

    
    def get_tasks(self, query=''):
        ''' get tasks '''
        try:
            endpoint = f'/intent/api/v1/task{query}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
            print(ex)

    
    def get_task_by_id(self, id):
        ''' get task status by id '''
        try:
            endpoint = f'/intent/api/v1/task/{id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)

    
    def get_task_tree(self, id):
        ''' get task tree '''
        try:
            endpoint = f'/intent/api/v1/task/{id}/tree'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




if __name__ == '__main__':

    dna_params_always_on = {
        'host': 'sandboxdnac2.cisco.com',
        'username': 'devnetuser',
        'password': 'Cisco123!',
    }

    dna_params_dcloud = {
        'host': 'dcloud-dna-center-inst-rtp.cisco.com',
        'username': 'demo',
        'password': 'demo1234!',
    }

    dna = DNA(**dna_params_always_on)
    # dna.get_sites()
    # dna.get_devices()
    # dna.get_device_config('6969b6dd-100c-4bc3-b284-df812f34f018')
    # dna.get_projects()
    # dna.get_event_count()
    # dna.get_event_subscriptions()
    # dna.get_templates()
    # dna.get_flow_analysis('/99a421ae-f474-43d5-9b4b-982f81cebee9')
    # dna.get_site_memberships("6d34d96d-d812-4afd-81ef-ba2d65dbf7ca")
    # dna.get_command_runner_legit_reads()
    # dna.get_device_count()
    # dna.get_site_health(query='?timestamp= &wirelessGoodClients=4')
    # dna.get_site_count()
    # dna.get_topolgy()
    # dna.get_network()
    # dna.get_service_provider_details()
    # dna.get_global_pool()
    # dna.get_devices(query='/6969b6dd-100c-4bc3-b284-df812f34f018')
    # dna.get_client_health()
    # dna.post_command_runner('Switches and Hubs', 'Cisco Catalyst 9300 Switch', 'show ver', 'show ip route')
    # dna.get_credentials_cli()
    # dna.get_credentials_snmp()
    # dna.get_device_discovery('my discovery', '10.0.0.0-10.255.255.255', timeout=1)
    # dna.get_events_assurance()
    # dna.post_subscribe_to_event('my sub', 'my desc', 'NETWORK-DEVICES-3-207')
    # dna.post_site()