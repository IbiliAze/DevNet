import requests
import json
import urllib3
from requests.exceptions import HTTPError
from pprint import pprint

class Meraki:

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self, meraki_api_key):
        self.meraki_api_key = meraki_api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Cisco-Meraki-API-Key': self.meraki_api_key
        }


    def req(self, method, endpoint, payload={}):
        ''' request helper function '''
        try: 
            response = requests.request(method=method, headers=self.headers,
                url=f'https://api.meraki.com/api/v0{endpoint}', json=payload)

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
        
        return response


    def get_net_id_by_name(self, network_name, org_id='962199'):
        networks = self.req('get', f'/organizations/{org_id}/networks').json()
        for network in networks:
            if network['name'] == network_name:
                network_id = network['id']
                return network_id
            else:
                raise ValueError('Network does not exist')




    ''' Organizations and Networks '''

    def get_organizations(self, organization=''):
        ''' get organizations '''
        try:
            endpoint = f'/organizations?organization={organization}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)

    
    def get_networks(self, organization_id='549236', query_string=''):
        ''' get networks '''
        try:
            endpoint = f'/organizations/{organization_id}/networks{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network(self, network_id='N_706502191543793968', query_string=''):
        ''' get a specific network '''
        try:
            endpoint = f'/networks/{network_id}{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_vpns(self, network_id='N_706502191543793968', query_string=''):
        ''' get site to site vpns '''
        try:
            endpoint = f'/networks/{network_id}/siteToSiteVpn{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_airmarshals(self, network_id='N_706502191543793968', query_string=''):
        ''' get network air marshals '''
        try:
            endpoint = f'/networks/{network_id}/airMarshal{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_access_policies(self, network_id='N_706502191543793968', query_string=''):
        ''' get network access policies '''
        try:
            endpoint = f'/networks/{network_id}/accessPolicies{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_traffic(self, network_id='N_706502191543793968', query_string=''):
        ''' get network access policies '''
        try:
            endpoint = f'/networks/{network_id}/traffic{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_network(self, organization_id, network_name, type):
        ''' create a network '''
        try:
            endpoint = f'/organizations/{organization_id}/networks'
            payload = {
                'name': network_name,
                'type': type
            }
            response = self.req('post', endpoint, payload)

            if response.status_code == 403:
                print('Not authorized')
            elif response.status_code == 201:
                print('Created the network')
                print(response.text)
            else:
                print(response.text)

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_organization(self, organization_name):
        ''' create an organization '''
        try:
            endpoint = f'/organizations'
            payload = {
                'name': organization_name,
                'type': 'appliance switch camera'
            }
            response = self.req('post', endpoint, payload)

            if response.status_code == 403:
                print('Not authorized')
            elif response.status_code == 201:
                print('Created the organization')
                print(response.text)
            else:
                print(response.text)

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Admins '''

    def get_admins(self, organization_id='549236', query_string=''):
        ''' get admins '''
        try:
            endpoint = f'/organizations/{organization_id}/admins{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_admins(self, name, email, organization_access, tag, access, organization_id='549236', query_string=''):
        ''' create admins '''
        try:
            payload = {
                "email": email,
                "name": name,
                "orgAccess": organization_access,
                "tags": [
                    {
                        "tag": tag,
                        "access": access
                    }
                ]
            }
            endpoint = f'/organizations/{organization_id}/admins{query_string}'
            response = self.req('post', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def delete_admins(self, organization_id, admin_id):
        ''' delete an admin '''
        try:
            endpoint = f'/organizations/{organization_id}/admins/{admin_id}'
            response = self.req('delete', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def put_admins(self, organization_id, admin_id, name, organization_access, tag, access):
        ''' update an admin profile '''
        try:
            payload = {
                "name": name,
                "orgAccess": organization_access,
                "tags": [
                    {
                        "tag": tag,
                        "access": access
                    }
                ]
            }
            endpoint = f'/organizations/{organization_id}/admins{admin_id}'
            response = self.req('put', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Devices '''

    def get_network_devices(self, network_id='N_706502191543793968', query_string='', serial=''):
        ''' get network devices '''
        try:
            if not serial:
                endpoint = f'/networks/{network_id}/devices{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            if serial:
                endpoint = f'/networks/{network_id}/devices/{serial}{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))


        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_network_device(self, network_id, *serials):
        ''' claim a network device '''
        try:
            payload = {'serials': [serial for serial in list(serials)]}
            endpoint = f'/networks/{network_id}/devices/claim'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_reboot_device(self, network_id, serial):
        ''' reboot a network device '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}/reboot'
            response = self.req('post', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_remove_device(self, network_id, serial):
        ''' remove a network device '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}/remove'
            response = self.req('post', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def put_device(self, network_id, serial, name, tags, notes, floorplan_id, address, longitude, latitude, query_string=''):
        ''' update a network device '''
        try:
            paylaod = {
                "name": name,
                "tags": tags,
                "lat": latitude,
                "lng": longitude,
                'address' : address,
                'notes': notes,
                'floorPlanId': floorplan_id
            }
            endpoint = f'/networks/{network_id}/devices/{serial}{query_string}'
            response = self.req('put', endpoint, paylaod).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_organization_devices(self, orgnazation_id, query_string=''):
        ''' get organization devices '''
        try:
            endpoint = f'/organizations/{orgnazation_id}/devices{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_uplink(self, network_id, serial, query_string=''):
        ''' get device uplink status '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}/uplink{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_performance(self, network_id, serial, query_string=''):
        ''' get device performance '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}/performance{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_loss_latency_history(self, network_id, serial, query_string=''):
        ''' get device uplink loss percentage and latency in milliseconds for a wired network device '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}/lossAndLatencyHistory{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_cdp_lldp_informatoon(self, network_id, serial, query_string=''):
        ''' get device cdp and lldp information '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}/lldp_cdp{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_cycle_ports(self, serial, *ports):
        ''' cycle a set of switchports '''
        try:
            payload = {'ports': [port for port in list(ports)]}
            endpoint = f'/devices/{serial}/switch/ports/cycle'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' SSID and Bluetooth information '''

    def get_ssids(self, network_id='N_706502191543793968', ssid_number = '', query_string=''):
        ''' get network ssids '''
        try:
            if ssid_number == '':
                endpoint = f'/networks/{network_id}/ssids{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/networks/{network_id}/ssids/{ssid_number}{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_wireless_status(self, network_id, serial):
        ''' get network device wireless status '''
        try:
            endpoint = f'/networks/{network_id}/devices/{serial}wireless/status'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def put_ssids(self, network_id, ssid_number, name, enabled):
        ''' update ssid information '''
        try:
            payload = {
                'name': name,
                'enabled': enabled
            }
            endpoint = f'/networks/{network_id}/ssids/{ssid_number}'
            response = self.req('put', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_bluetooth_clients(self, network_id, client_id='', query_string=''):
        ''' get bluetooth clients '''
        try:
            if client_id == '':
                endpoint = f'/networks/{network_id}/bluetoothClients{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/networks/{network_id}/bluetoothClients/{client_id}{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_bluetooth_settings(self, serial, query_string):
        '''get device bluetooth settings '''
        try:
            endpoint = f'/devices/{serial}/wireless/bluetooth/settings{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_bluetooth_settings(self, network_id, query_string=''):
        ''' get network bluetooth settings '''
        try:
            endpoint = f'/networks/{network_id}/bluetoothSettings{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' HTTP Servers '''

    def get_http_servers(self, network_id, query_string=''):
        ''' get network http servers '''
        try:
            endpoint = f'/networks/{network_id}/httpServers{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_http_server_webhooktest(self, network_id, id):
        ''' get the status of a webhook test for a network '''
        try:
            endpoint = f'/networks/{network_id}/httpServers/{id}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_http_server(self, url, network_id, name, shared_secret):
        ''' add a webhook receiver '''
        try:
            if not url.startswith('https'):
                print('The HTTP server must be on a secure HTTPS TLS connection')
            elif url.startswith('https'):
                endpoint = f'/networks/{network_id}/httpServers'
                payload = {
                  "id": "ABC123",
                  "networkId": network_id,
                  "name": name,
                  "url": url,
                  "sharedSecret": shared_secret
                }
                response = self.req('post', endpoint, payload)

                if response.status_code == 403:
                    print('Not authorized')
                elif response.status_code == 401:
                    print('Not authenticated')
                elif response.status_code == 201:
                    print('Added the HTTP Servers')
                    print(response.text)
                else:
                    print(response.text)
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)

        
    def delete_http_server(self, network_id, server_id):
        ''' delete an http server '''
        try:
            endpoint = f'/networks/{network_id}/httpServers/{server_id}'
            response = self.req('delete', endpoint)
            print(response.text)
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_http_server_webhooktest(self, network_id, url):
        ''' send a test webhook for a network '''
        try:
            payload = {
                'url': url
            }
            endpoint = f'/networks/{network_id}/httpServers/webhookTests'
            response = self.req('post', endpoint, payload)

            if response.status_code == 403:
                print('Not authorized')
            elif response.status_code == 201:
                print('Created the organization')
                print(response.text)
            else:
                print(response.text)

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
        



    ''' Monitoring and Alerting '''

    def get_webhook_logs(self, organization_id):
        ''' get the log of webhook posts sent '''
        try:
            endpoint = f'/organizations/{organization_id}/webhookLogs'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_latency_stats(self, network_id, query_string=''):
        ''' get wireless latency stats '''
        try:
            endpoint = f'/networks/{network_id}/latencyStats{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_connection_stats(self, network_id, query_string=''):
        ''' get network connection stats '''
        try:
            endpoint = f'/networks/{network_id}/connectionStats{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_failed_connections(self, network_id, query_string=''):
        ''' get wireless failed connections '''
        try:
            endpoint = f'/networks/{network_id}/failedConnections{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_latency_stats(self, network_id, device_sn='', query_string=''):
        ''' get device latency stats '''
        try:
            endpoint = f'/networks/{network_id}/devices/{device_sn}/latencyStats{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_device_connection_stats(self, network_id, device_sn='', query_string=''):
        ''' get device connection stats '''
        try:
            endpoint = f'/networks/{network_id}/devices/{device_sn}/connectionStats{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_latency_stats(self, network_id, client_id='', query_string=''):
        ''' get client latency stats '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/latencyStats{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_connection_stats(self, network_id, client_id='', query_string=''):
        ''' get client connection stats '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/connectionStats{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_api_usage_stats(self, organization_id, query_string=''):
        ''' get api usage stats '''
        try:
            endpoint = f'/organizations/{organization_id}/apiRequests{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_api_usage_stats_overview(self, organization_id, query_string=''):
        ''' get api usage stats overview '''
        try:
            endpoint = f'/organizations/{organization_id}/apiRequests/overview{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_alerts_settings(self, network_id, query_string=''):
        ''' get network alert settings '''
        try:
            endpoint = f'/networks/{network_id}/alertSettings{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
        

    def put_alert_settings(self, network_id, type, snmp=True, enabled=True, timeout=60, *emails):
        ''' update network alert settings '''
        try:
            payload = {
                "defaultDestinations": {
                    "emails": list(emails),
                        "allAdmins": True,
                        "snmp": snmp
                },
                "alerts": [
                    {
                        "type": "gatewayDown",
                        "enabled": enabled,
                        "alertDestinations": {
                            "emails": list(emails),
                            "allAdmins": True,
                            "snmp": snmp
                        },
                        "filters": {
                            "timeout": timeout
                        }
                    }
                ]
            }
            endpoint = f'/networks/{network_id}/alertSettings'
            response = self.req('put', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_events(self, network_id, query_string=''):
        ''' get network events '''
        try:
            endpoint = f'/networks/{network_id}/events{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_event_types(self, network_id, query_string=''):
        ''' get network event types '''
        try:
            endpoint = f'/networks/{network_id}/events/eventTypes{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' MV-Sense API '''

    def get_mvsense_feed(self, serial, timeframe):
        '''get live state of camera analytics '''
        try:
            endpoint = f'/devices/{serial}/camera/analytics/{timeframe}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_mvsense_zones(self, serial):
        '''get camera zone history '''
        try:
            endpoint = f'/devices/{serial}/camera/analytics/zones'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_mvsense_zone_history(self, serial, zone_id):
        '''get camera zone history '''
        try:
            endpoint = f'/devices/{serial}/camera/analytics/zones/{zone_id}/history'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_camera_qr_profile(self, network_id, qr_profile_id='', query_string=''):
        '''get quality and retention profile '''
        try:
            if qr_profile_id != '':
                endpoint = f'/networks/{network_id}/camera/qualityRetentionProfiles/{qr_profile_id}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/networks/{network_id}/camera/qualityRetentionProfiles{query_string}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_camera_qr_profile(self, network_id, name):
        ''' create a quality and retention profile '''
        try:
            payload = {
                "name": name
            }
            endpoint = f'/networks/{network_id}/camera/qualityRetentionProfiles'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_camera_snapshot(self, network_id, serial):
        ''' perform a camera snapshot '''
        try:
            payload = {}
            endpoint = f'/networks/{network_id}/camera/{serial}/snapshot'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_camera_link(self, network_id, serial, query_string=''):
        ''' get a link of the camera '''
        try:
            endpoint = f'/networks/{network_id}/cameras/{serial}/videoLink{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_camera_video_settings(self, serial):
        ''' get device camera video settings '''
        try:
            endpoint = f'/devices/{serial}/camera/video/settings'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_camera_schedules(self, network_id):
        ''' get network camera recording schedules '''
        try:
            endpoint = f'/networks/{network_id}/camera/schedules'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Clients '''

    def get_device_clients(self, serial, client_id = '', query_string=''):
        ''' get clients connected to a device '''
        try:
            if client_id == '':
                endpoint = f'/devices/{serial}/clients'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/devices/{serial}/clients/{client_id}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_network_clients(self, network_id, query_string=''):
        ''' get network clients '''
        try:
            endpoint = f'/networks/{network_id}/clients{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_events(self, network_id, client_id, query_string=''):
        ''' get client events '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/events{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_latency_history(self, network_id, client_id, query_string=''):
        ''' get client latency history '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/latencyHistory{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_policy(self, network_id, client_id, query_string=''):
        ''' get client policy '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/policy{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_autho_status(self, network_id, client_id, query_string=''):
        ''' get client splash authorization status '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_traffic_history(self, network_id, client_id, query_string=''):
        ''' get client traffic history '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/trafficHistory{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_client_usage_history(self, network_id, client_id, query_string=''):
        ''' get client usage history '''
        try:
            endpoint = f'/networks/{network_id}/clients/{client_id}/usageHistory{query_string}'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_client_provosioning(self, network_id, device_policy, group_policy_id):
        ''' post client group policy '''
        try:
            payload = {
                'devicePolicy': device_policy,
                'groupPolicyId': group_policy_id
            }
            endpoint = f'/networks/{network_id}/clients/provision'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Splash Page '''

    def get_splash_login_attempts(self, network_id, query_string=''):
        ''' get splash page login attempts '''
        try:
            endpoint = f'/networks/{network_id}/splashLoginAttempts'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def get_splash_settings(self, network_id, ssid_number):
        ''' get splash page settings for a given ssid '''
        try:
            endpoint = f'/networks/{network_id}/ssids/{ssid_number}/splashSettings'
            response = self.req('get', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def put_netowrk_splash_settings(self, network_id, ssid_number, splash_url, use_splash_url=True):
        ''' update splash page settings for a given ssid '''
        try:
            payload = {
                "splashUrl": splash_url,
                "useSplashUrl": use_splash_url
            }
            endpoint = f'/networks/{network_id}/ssids/{ssid_number}/splashSettings'
            response = self.req('put', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)




    ''' Static Routes '''

    def get_static_routes(self, network_id, route_id=''):
        '''get static routes '''
        try:
            if route_id != '':
                endpoint = f'/networks/{network_id}/staticRoutes/{route_id}'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))
            else:
                endpoint = f'/networks/{network_id}/staticRoutes'
                response = self.req('get', endpoint).json()
                print(json.dumps(response, indent=2, sort_keys=True))

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def post_static_routes(self, network_id, name, subnet, gateway_ip):
        ''' create a static route '''
        try:
            payload = {
                "name": name,
                "subnet": subnet,
                "gatewayIp": gateway_ip
            }
            endpoint = f'/networks/{network_id}/staticRoutes'
            response = self.req('post', endpoint, payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def delete_static_routes(self, network_id, route_id):
        ''' delete static routes '''
        try:
            endpoint = f'/networks/{network_id}/staticRoutes/{route_id}'
            response = self.req('delete', endpoint).json()
            print(json.dumps(response, indent=2, sort_keys=True))
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)





if __name__ == '__main__':
    
    meraki_params_always_on = {
        'meraki_api_key': ''
    }
    
    meraki = Meraki(**meraki_params_always_on)
    # meraki.get_mvsense_feed('efef', 'live')
    # meraki.get_static_routes('N_706502191543793968')
    # meraki.get_bluetooth_clients('N_706502191543793968')
    # meraki.get_network_bluetooth_settings('N_706502191543793968')
    # meraki.get_ssids('N_706502191543793968')
    # meraki.post_network('962199', 'Wireless Network', 'wireless')
    # meraki.get_networks('962199')
    # meraki.get_network_clients('N_706502191543793968')
    # meraki.get_ssids('N_706502191543803223', 13)
    # meraki.put_ssids('N_706502191543803223', 13, 'My SSID', True)
    # meraki.get_airmarshals()
    # meraki.get_network_events('N_706502191543793968')
    # meraki.get_network_event_types('N_706502191543793968')
    # meraki.get_api_usage_stats('962199')
    # meraki.get_organization_devices(orgnazation_id='962199')
    # meraki.post_network_device('N_706502191543793968', 'ferfe', 'efeef', 'efefef')
    # meraki.get_client_connection_stats('N_706502191543793968', query_string='?timespan=300')
    # meraki.get_latency_stats('N_706502191543793968', '?timespan=322')
    # meraki.get_failed_connections('N_706502191543793968', '?timespan=322')
    # meraki.get_client_latency_stats(meraki.get_net_id_by_name('My Site'), query_string='?timespan=232')
    # meraki.get_organizations('962199')
    # meraki.post_organization('My Enauto Org')
    # meraki.get_networks(organization_id='962199')
    # meraki.get_devices()
    # meraki.get_ssids()
    # meraki.get_admins()
    # meraki.post_network(organization_id='962199', network_name='KRK Network')
    # meraki.post_http_server('https://2b7b4ebd.ngrok.io', 'L_706502191543756137',
    #     'Webhook Receiver 1', 'foofoo' )
    # meraki.get_networks(organization_id='962199')
    # meraki.get_network_vpns(network_id='N_706502191543793968')
    # meraki.get_network_air_marshals(network_id='N_706502191543793968')
    # meraki.get_network_access_policies(network_id='N_706502191543793968')
    # meraki.get_network_traffic(network_id='N_706502191543793968', query_string='?timespan=1760')
    # meraki.get_network(network_id='N_706502191543793968')
    # meraki.get_admins(organization_id='962199', query_string='/1181841')
    # meraki.get_devices(network_id='N_706502191543793968')
    # meraki.get_ssids(network_id='N_706502191543793968')
    # meraki.post_network(organization_id='962199', network_name='Test3')
    # meraki.post_http_server('https://www.google.com', 'N_706502191543793968', 'Webhook Receiver', 'fooo')
    # meraki.delete_http_server('N_706502191543793968', 'aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbQ==')
    # meraki.get_http_servers('N_706502191543793968')
    # meraki.get_webhook_logs(organization_id='962199')