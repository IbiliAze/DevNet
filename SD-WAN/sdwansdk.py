import json
import requests
import urllib3
from requests.exceptions import HTTPError
from pprint import pprint
from datetime import datetime



class SD_WAN:
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def __init__(self, host, port, username, password):

        ''' login attributes '''
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        path = 'j_security_check'
        url = f"https://{self.host}:{self.port}/{path}"
        body = {
            'j_username': self.username,
            'j_password': self.password
        }
        try:
            ''' storing the cookie in a session '''
            with requests.session() as self.session:
                response = self.session.post(url, data=body, 
                    verify=False)
                if not response.ok or response.text:
                    print('Login failed.')
                    print()
                else:
                    print('Login succeeded')
                    print()

        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)


    def req(self, method, endpoint, payload={}, params={}, print_output=False, dictionary=False):
        ''' request helper function '''
        session = self.session

        try:
            if print_output == False and dictionary == False:
                response = session.request(method, url=f"https://{self.host}:{self.port}/dataservice{endpoint}", json=payload,
                    params=params, verify=False)
                return response

            elif print_output == True and dictionary == False:
                response = session.request(method, url=f"https://{self.host}:{self.port}/dataservice{endpoint}", json=payload,
                    params=params, verify=False)
                pprint(response.text)
                return response

            elif print_output == False and dictionary == True:
                response = session.request(method, url=f"https://{self.host}:{self.port}/dataservice{endpoint}", json=payload,
                    params=params, verify=False).json()
                return response

            elif print_output == True and dictionary == True:
                response = session.request(method, url=f"https://{self.host}:{self.port}/dataservice{endpoint}", json=payload,
                    params=params, verify=False).json()
                print(json.dumps(response, indent=2, sort_keys=True))
                return response
        except HTTPError as http:
            print(http)
        except Exception as ex:
            print(ex)
            

    def save_to_file(self, api_call):
        with open(f'SD-WAN/{datetime.now().date()}.json', 'w') as handle:
            json.dump(api_call, handle, indent=2, sort_keys=True)



    ''' Alarms '''

    def get_alarm_count(self):
        ''' get alarms count '''
        return self.req('get', '/alarms/count', dictionary=True, print_output=True)


    def get_alarms(self, query=''):
        ''' get alarms '''
        return self.req('get', f'/alarms{query}', dictionary=True, print_output=True)




    ''' Certificates '''

    def get_certificate_summary(self):
        ''' get certificate health summary '''
        return self.req('get', '/certificate/stats/summary', dictionary=True, print_output=True)


    def get_certificates(self):
        ''' get all certificates '''
        return self.req('get', '/certificate/vsmart/list', dictionary=True, print_output=True)


    def get_root_certificate(self):
        ''' get root certificate '''
        return self.req('get', '/certificate/rootcertificate', dictionary=True, print_output=True)




    ''' Device Control and Audit Trail '''

    def get_device_control_status(self):
        ''' get number of online vedge devices '''
        return self.req('get', '/device/control/count', dictionary=True, print_output=True)
        

    def get_device_tunnel_statistics(self, device_id):
        ''' get tunnel statistics '''
        return self.req('get', '/device/tunnel/statistics', params={'deviceId': device_id}, dictionary=True, print_output=True)


    def get_device_control_connections(self, device_id):
        ''' get device control connection statistics '''
        return self.req('get', '/device/control/connections', params={'deviceId': device_id}, dictionary=True, print_output=True)


    def post_audit(self, condition='AND', field='entry_time', value='1', type='date', operator='last_n_hours'):
        ''' query system performance '''
        payload = {
            'query':{
                'condition': condition,
                'rules': [
                    {
                        'field': 'vdevice_name', # what is being evaluated
                        'type': 'string',
                        'value': ['4.4.4.90'], # value that must be matched compared against the field
                        'operator': 'in' # how to compare
                    }
                ]
            },
            'size': 2,
            'fields': ['entry_time', 'mem_util', 'device_model', 'cpu_user', 'host_name', 'vdevice_name']
        }
        return self.req('post', '/statistics/system', payload=payload, print_output=True, dictionary=True)


    def get_auditlog(self):
        ''' get auditlog '''
        return self.req('get', '/auditlog', dictionary=True, print_output=True)




    ''' Admins '''

    def get_admin_users(self):
        response = self.req('get', '/admin/user').json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response


    def post_admin_user(self, username, password, *group):
        payload = {
            'group' : list(group),
            'description': 'Admin Data',
            'userName': username,
            'password': password
        }
        response = self.req('post', '/admin/user', body=payload).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response


    def put_user_password(self, username, new_password):
        payload = {
            'userName': username,
            'password': new_password
        }
        response = self.req('put', f'/admin/user/password/{username}', body=payload)
        pprint(response.text)
        return response


    def delete_user(self, username):
        payload = {}
        response = self.req('delete', f'/admin/user/{username}', body=payload).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response


    def get_admin_usergroups(self):
        ''' get groups '''
        return self.req('get', '/admin/usergroup', print_output=True, dictionary=True)


    def post_group(self, name, read, write, enabled, *features):
        ''' create a new group '''
        payload = {
            'groupName': name,
            'tasks': [
                {
                    'feature': feature,
                    'read': read,
                    'write': write,
                    'enabled': enabled
                } for feature in list(features)
            ]
        }
        return self.req('post', '/admin/usergroup', payload, print_output=True, dictionary=True)


    def get_user_role(self):
        ''' get user roles '''
        return self.req('get', '/admin/user/role', print_output=True, dictionary=True)




    ''' Devices '''

    def get_devices(self, model=''):
        response = self.req('get', '/device', 
            params={'model': model} if model else None).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response


    def get_vedges(self, model=''):
        response = self.req('get', '/system/device/vedges', 
            params={'model': model} if model else None).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response

    
    def get_vmanages(self, model=''):
        response = self.req('get', '/system/device/vmanages', 
            params={'model': model} if model else None).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response


    def get_device_controllers(self, model=''):
        response = self.req('get', '/system/device/controllers', 
            params={'model': model} if model else None).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response
        



    ''' Templates '''

    def get_feature_templates(self, query=''):
        ''' get feature templates '''
        return self.req('get', f'/template/feature{query}', dictionary=True, print_output=True)


    def get_device_templates(self):
        ''' see what templates are attached to which devices '''
        return self.req('get', '/template/device', dictionary=True, print_output=True)


    def post_device_feature_template(self, template_name, device_type='vsmart', *template_id):
        ''' create a device template that contains feature templates '''
        payload = {
            "policyId": "",
            "templateDescription": f"{template_name} DESCRIPTION",
            "templateName": template_name,
            "configType": "template",
            "deviceType": device_type,
            "factoryDefault": False,
            "featureTemplateUidRange": [],
            "generalTemplates": [
                {'templateId': template} for template in list(template_id)
            ]        
        }
        return self.req('post', '/template/device/feature', payload=payload, dictionary=True, print_output=True)


    def post_template_to_device(self, template_id, *device_ids):
        ''' assign a device template to a device '''
        payload = {
            'templateId': template_id,
            'deviceIds': list(device_ids),
            'isEdited': False,
            'isMasterEdited': False
        }
        return self.req('post', '/template/device/config/input', payload=payload, dictionary=True, print_output=True)





    ''' Policy '''

    def get_policy(self):
        response = self.req('get', '/template/policy/list').json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response


    def _post_policy(self, name, description, object_type, entries):
        try:
            payload = {
                'name': name,
                'description': description,
                'type': object_type,
                'entries': entries
            }
            response = self.req('post', f'/template/policy/list/{object_type}', body=payload).json()
            print(json.dumps(response, indent=2, sort_keys=True))
            if not response['listId']:
                print('Already created')
            return response
        except Exception as ex:
            print(ex)


    def post_policy_site(self, name, site_list):
        entries = [{'siteId': str(site)} for site in site_list]
        response = self._post_policy(object_type='site', name=name, entries=entries, description='')
        return response


    def post_policy_vpn(self, name, vpn_list):
        entries = [{'vpn': str(vpn)} for vpn in vpn_list]
        response = self._post_policy(object_type='vpn', name=name, entries=entries, description='')
        return response


    def post_policy_sla(self, name, sla_entries):
        response = self._post_policy(object_type='sla', name=name, entries=sla_entries, description='')
        return response


    def post_policy_mesh(self, name, vpn_id, region_map, description='none'):
        regions = []
        for region, site_id in region_map.items():
            regions.append({'name': region, 'siteLists': site_id})
        payload = {
            'name': name,
            'type': 'mesh',
            'description': description,
            'definition': {'vpnList': vpn_id, 'regions': regions}
        }
        response = self.req('post', '/template/policy/definition/mesh', body=payload).json()
        print(json.dumps(response, indent=2, sort_keys=True))
        return response




if __name__ == "__main__":

    sdwan_params_always_on = {
        'host': 'sandboxsdwan.cisco.com',
        'port': '8443',
        'username': 'devnetuser',
        'password': 'Cisco123!',
    }
    
    sdwan_params_reserved = {
        'host': '10.10.20.90',
        'port': '443',
        'username': 'admin',
        'password': 'admin',
    }

    sdwan = SD_WAN(**sdwan_params_reserved)
    # sdwan.post_audit()
    # sdwan.get_auditlog()
    sdwan.get_user_role()
    # sdwan.get_admin_usergroups()
    # sdwan.post_group('audit', True, True, True, 'Audit Log', 'Interface', 'System')
    # sdwan.get_feature_templates()
    # sdwan.get_devices()
    # sdwan.get_vedges()
    # sdwan.get_alarm_count()
    # sdwan.get_alarms()
    # sdwan.get_device_control_status()
    # sdwan.get_certificate_summary()
    # sdwan.get_device_tunnel_statistics('4.4.4.65')
    # sdwan.get_device_control_connections('4.4.4.65')
    # sdwan.get_admin_users()
    # sdwan.delete_user('ibi2')
    # sdwan.post_admin_user('devuser', 'cisco', 'netadmin')
    # sdwan.put_user_password('ibi', 'Cisco123!')
    # sdwan.get_admin_user_groups()
    # print(sdwan.get_admin_user_groups.__name__)
    # sdwan.get_vedges_saved_to_file()
    # sdwan.get_device_controllers()
    # sdwan.save_to_file(sdwan.get_feature_templates())
    # sdwan.get_device_templates()
    # sdwan.get_policy()
    # sdwan.post_attach_vsmart_device_template()
    # sdwan.get_feature_templates()
    # sdwan.post_device_template('vManage Template5', 'vmanage', '1918ba5d-e91d-4682-b889-71fd5fd27765', 'bf3fcac8-8ab3-46a3-9ab5-c0d3e6107826')
    # sdwan.get_device_templates()
    # sdwan.post_template_to_device('767352d6-5c7a-471a-8277-cd243830dd2b', 'b354bdfc-4d49-4c75-a407-ae59087758db', 'ddd801b2-8cbe-4394-abd1-3b71e39886e3')
    # sdwan.get_vmanages()
    # sdwan.post_device_template()
    # sdwan.post_template('d602cad0-bdb9-418a-95c3-74ff6fda3373', '1920C431170635')
    sdwan.get_alarms('/count')
    # sdwan.get_root_certificate()
    # sdwan.get_device_templates()
 







    ''' QUERY RANDOM '''
    
    def create_templates(var_map, template_name='New', device_type='vsmart'):
        fts = sdwan.get_feature_templates()
        vsmart_temp_ids = []
        for ft in fts['data']:
            if ft['templateType'].endswith('vsmart'):
                vsmart_temp_ids.append(ft['templateId'])
        sdwan.post_device_template(template_name, device_type, vsmart_temp_ids)

        templates = sdwan.get_device_templates()['data']
        for template in templates:
            if template['templateName'] == template_name:
                template_id = template['templateId']

        templates = []
        vsmarts = sdwan.get_devices(model='vsmart')['data']
        for vsmart in vsmarts:
            site_id, def_gateway = var_map[vsmart['hostname']]
    # create_templates()


    def create_policy():
        try:
            site_policy = sdwan.post_policy_site('Leeds', [400])
            vpn_policy = sdwan.post_policy_vpn('Engineering', [3])
            sla_policy = sdwan.post_policy_sla('Voice', [{'latency': '150', 'loss':'1', 'jitter':'30'}])

            policies = sdwan.get_policy()['data']
            for policy in policies:
                if policy['name'] == 'Leeds':
                    site_id = policy['listId']

            for policy in policies:
                if policy['name'] == 'Engineering':
                    vpn_id = policy['listId']

            for policy in policies:
                if policy['name'] == 'Voice':
                    sla_id = policy['listId']

            print(site_id)
            print(vpn_id)
            print(sla_id)
        except Exception as ex:
            print(ex)
    # create_policy()



    ''' QUERY with REQ FUNCTION '''


    ''' get vedges '''
    # response = sdwan.req('get', '/system/device/vedges').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


    ''' get fts '''
    # response = sdwan.req('get', '/template/feature').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


    ''' get fts '''
    # response = sdwan.req('get', '/certificate/rootcertificate').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


    ''' get fts '''
    # response = sdwan.req('get', '/alarms/count').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


    ''' get fts '''
    # response = sdwan.req('get', '/certificate/stats/summary').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


    ''' get fts '''
    # response = sdwan.req('get', '/device/control/count').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


    ''' get fts '''
    # response = sdwan.req('get', '/template/feature').json()
    # print(json.dumps(response, indent=2, sort_keys=True))


