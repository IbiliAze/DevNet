from netmiko import ConnectHandler
from ncclient import manager
from yaml import safe_load
import json
from jinja2 import Environment, FileSystemLoader
from ncclient import manager
import xmltodict
from lxml.etree import fromstring


class GNS3:

    def __init__(self, host, username, password, connection_type, port='22', device_type='cisco_ios'):

        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type
        self.connection_type = connection_type

        if connection_type == 'netconf':
            self.port = port
            self.netconf_connection = manager.connect(host=self.host, port=self.port, username=self.username, 
                password=self.password, hostkey_verify=False)

        elif connection_type == 'ssh':
            self.connection = ConnectHandler(ip=self.ip, username=self.username,
                password=self.password, device_type=self.device_type)
        

    def dhcp(self, address_range):
        dhcp_commands = ['']


    def get_netconf_capabilities(self):
        try:
            with self.netconf_connection as netconf_connection:
                for capability in netconf_connection.server_capabilities:
                    print(capability)
        except Exception as ex:
            print(ex)


    def subscribe_to_netconf_event(self, period, *subscription_urn):
        subs = list(subscription_urn)
        for sub in subs:
            rpc = f'''
                <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
                    <stream>yp:yang-push</stream>
                    <yp:xpath-filter>{sub}</yp:xpath-filter>
                    <yp:period>{period}</yp:period>
                </establish-subscription>
            '''
            response_xml = self.netconf_connection.dispatch(fromstring(rpc))
            response = xmltodict.parse(response_xml.xml)
            print(json.dumps(response, indent=2, sort_keys=True))

            counter = 0
            while counter < 5:
                subscription_data_xml = self.netconf_connection.take_notification()
                subscription_data = xmltodict.parse(subscription_data_xml.notification_xml)
                print(json.dumps(subscription_data, indent=2, sort_keys=True))
                counter = counter + 1
        

    def interfaces(self, *interfaces):
        ''' create interfaces '''
        for interface in list(interfaces):
            interface_name = list(interface.keys())[0]
            ip_address = list(interface.values())[0]
            interface_commands = [f'interface {interface_name}', f'ip address {ip_address}', 'no shut']
            interface_config = self.connection.send_config_set(interface_commands)
            print(interface_config)


    def ospf(self,  *ip_addresses, wildcard_bits='0.0.0.0', area='0',):
        ''' ospf config '''
        for ip_address in list(ip_addresses):
            ospf_commands = ['router ospf 1', f'network {ip_address} {wildcard_bits} area 0']
            ospf_config = self.connection.send_config_set(ospf_commands)
            print(ospf_config)


    def domain_lookup(self):
        try:
            with open('GNS3/vars.yml', 'r') as handle:
                host_root = safe_load(handle)
            jinja_environment = Environment(loader=FileSystemLoader('.'), autoescape=True)
            template = jinja_environment.get_template('GNS3/template.j2')
            dns_commands = template.render(data=host_root)
            dns_config = self.connection.send_config_set(dns_commands.split('\n'))
            print(dns_config)
            self.connection.disconnect()
        except Exception as ex:
            print(ex)

    def priv(self, command):
        print(self.connection.send_command(command))


if __name__ == '__main__':

    router = {
        'ip': '192.168.0.59',
        'username': 'ibi',
        'password': 'cisco',
        'device_type': 'cisco_ios'
    }

    ios_xe = {
        'host': 'ios-xe-mgmt-latest.cisco.com',
        'port': '10000',
        'username': 'developer',
        'password': 'C1sco12345'
    }

    gns3 = GNS3(**ios_xe, connection_type='netconf')
    # gns3.interfaces({'fa0/1':'20.1.1.1 255.255.255.0'}, {'fa1/0':'30.1.1.1 255.255.255.0'})
    # gns3.ospf('20.1.1.1', '30.1.1.1')
    # gns3.domain_lookup()
    # gns3.priv('show run')
    # gns3.get_netconf_capabilities()
    gns3.subscribe_to_netconf_event('500', '/mdt-oper:mdt-oper-data/mdt-subscriptions')

