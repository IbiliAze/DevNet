import xml.dom.minidom as mini
from pprint import pprint
import json
import xmltodict
from ncclient import manager

host = 'ios-xe-mgmt-latest.cisco.com'
port = '10000'
user = 'developer'
password = 'C1sco12345'


def get_capablities():
    router = {
        'host':host, 
        'port': port, 
        'username': user, 
        'password': password,
        'hostkey_verify': False
    }
    try:
        with manager.connect(**router) as connection:
            for capability in connection.server_capabilities:
                print(capability)
    except Exception as e:
        print(e)
        # raise "Connection Failed"


def get_interface_stats(int):
    try:
        netconf_filter = f"""
        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{int}</name>
                </interface>
            </interfaces>
            <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{int}</name>
                </interface>
            </interfaces-state>
        </filter>
        """
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            interface_netconf = connection.get(netconf_filter)
        xmlDom = mini.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent="  "))
        print()
        interface_python = xmltodict.parse(interface_netconf.xml)[
            "rpc-reply"]["data"]
        print(json.dumps(interface_python, indent=2, sort_keys=True))
        name = interface_python['interfaces']['interface']['name']['#text']
        print(name)

        config = interface_python["interfaces"]["interface"]
        op_state = interface_python["interfaces-state"]["interface"]

        print("Start")
        print(f"Name: {config['name']['#text']}")
        print(f" -Description: {config['description']}")
        print(f"  -Pakcets In: {op_state['statistics']['in-unicast-pkts']}")
    except Exception as e:
        print(e)


def edit_int():
    try:
        config_template = '''
        <config>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{interface_name}</name>
                    <description>{interface_desc}</description>
                    <enabled>true</enabled>
                </interface>
            </interfaces>
        </config>
        '''
        netconf_config = config_template.format(
            interface_name='GigabitEthernet3', interface_desc='lel'
        )
        with manager.connect(host=host, port=port, username=user, password=password,
                             hostkey_verify=False) as connection:
            response = connection.edit_config(netconf_config, target="running")
            response_dict = xmltodict.parse(response.xml)
            print(response_dict)
            # print(json.dumps(response, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_running_config():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            response = connection.get_config("running")
            running_config = xmltodict.parse(response.xml)
            print(mini.parseString(response.xml).toprettyxml())
            # print(json.dumps(running_config, indent=2, sort_keys=True))
            return running_config
    except Exception as e:
        print(e)


def get_startup_config():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            response = connection.get_config("startup")
            startup_config = xmltodict.parse(response.xml)
            print(json.dumps(startup_config, indent=2, sort_keys=True))
            return startup_config
    except Exception as e:
        print(e)


def get_routing_info():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
                    <routing-instance>
                        <name>default</name>
                    </routing-instance>
                </routing>
            </filter>
            '''
            response = connection.get(netconf_filter)
            # print(mini.parseString(response.xml).toprettyxml())
            routing_info = xmltodict.parse(response.xml)
            print(json.dumps(routing_info, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_ospf_info():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <router>
                        <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                        </ospf>
                    </router>     
                </native>
            </filter>
            '''
            response = connection.get(netconf_filter)
            print(mini.parseString(response.xml).toprettyxml())
            ospf_info = xmltodict.parse(response.xml)
            # print(json.dumps(ospf_info, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_bgp_info():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <router>
                        <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
                        </bgp>
                    </router>
                </native>
            </filter>
            '''
            response = connection.get_config("running", netconf_filter)
            # print(mini.parseString(response.xml).toprettyxml())
            bgp_info = xmltodict.parse(response.xml)
            print(json.dumps(bgp_info, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def edit_ospf(procesId, network, wildcardBits, areaId, routerId):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            config_template = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <router>
                                <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                                        <id>{id}</id>
                                        <vrf>IPN</vrf>
                                        <auto-cost>
                                                <reference-bandwidth>100000</reference-bandwidth>
                                        </auto-cost>
                                        <log-adjacency-changes>
                                                <detail/>
                                        </log-adjacency-changes>
                                        <passive-interface>
                                                <default/>
                                        </passive-interface>
                                        <router-id>{router_id}</router-id>
                                        <network>
                                                <ip>{ip}</ip>
                                                <mask>{mask}</mask>
                                                <area>{area}</area>
                                        </network>
                                </ospf>
                        </router>
                </native>
            </config>
            '''
            netconf_config = config_template.format(
                id=procesId,
                router_id=routerId,
                ip=network,
                mask=wildcardBits,
                area=areaId
            )
            response = connection.edit_config(netconf_config, target="running")
            # print(mini.parseString(response.xml).toprettyxml())
            response_dict = xmltodict.parse(response.xml)
            print(json.dumps(response_dict, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def delete_ospf(procesId, network, wildcardBits, areaId, routerId):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            config_template = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <router>
                                <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf" operation="delete">
                                        <id>{id}</id>
                                        <vrf>IPN</vrf>
                                        <auto-cost>
                                                <reference-bandwidth>100000</reference-bandwidth>
                                        </auto-cost>
                                        <log-adjacency-changes>
                                                <detail/>
                                        </log-adjacency-changes>
                                        <passive-interface>
                                                <default/>
                                        </passive-interface>
                                        <router-id>{router_id}</router-id>
                                        <network>
                                                <ip>{ip}</ip>
                                                <mask>{mask}</mask>
                                                <area>{area}</area>
                                        </network>
                                </ospf>
                        </router>
                </native>
            </config>
            '''
            netconf_config = config_template.format(
                id=procesId,
                router_id=routerId,
                ip=network,
                mask=wildcardBits,
                area=areaId
            )
            response = connection.edit_config(netconf_config, target="running")
            # print(mini.parseString(response.xml).toprettyxml())
            response_dict = xmltodict.parse(response.xml)
            print(json.dumps(response_dict, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_users():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <username>
                    </username>
                </native>
            </filter>
            '''
            response = connection.get(netconf_filter)
            # print(mini.parseString(response.xml).toprettyxml())
            usernames = xmltodict.parse(response.xml)
            print(json.dumps(usernames, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def edit_user(u, p, pl):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            config_template = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <username>
                        <name>{user}</name>
                            <privilege>{privilege_level}</privilege>
                            <password>
                                    <encryption>0</encryption>
                                    <password>{pw}</password>
                            </password>
                    </username>
                </native>
            </config>
            '''
            netconf_config = config_template.format(
                user=u, privilege_level=pl, pw=p
            )
            response = connection.edit_config(netconf_config, target="running")
    except Exception as e:
        print(e)


def delete_user(u, p, pl):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            config_template = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <username operation="delete">
                        <name>{user}</name>
                            <privilege>{privilege_level}</privilege>
                            <password>
                                    <encryption>0</encryption>
                                    <password>{pw}</password>
                            </password>
                    </username>
                </native>
            </config>
            '''
            netconf_config = config_template.format(
                user=u, privilege_level=pl, pw=p
            )
            response = connection.edit_config(netconf_config, target="running")
    except Exception as e:
        print(e)


def get_crypto():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <crypto/>
                </native>
            </filter>
            '''
            response = connection.get(netconf_filter)
            print(mini.parseString(response.xml).toprettyxml())
            crypto_config = xmltodict.parse(response.xml)
            print(json.dumps(crypto_config, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_ip_route():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <route/>
                    </ip>
                </native>
            </filter>
            '''
            response = connection.get_config("running", netconf_filter)
            print(mini.parseString(response.xml).toprettyxml())
            ip_route = xmltodict.parse(response.xml)
            print(json.dumps(ip_route, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def edit_ip_route(destination, subnet_mask, next_hop, interface):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <route>
                            <ip-route-interface-forwarding-list>
                                <prefix>{ip}</prefix>
                                <mask>{mask}</mask>
                                <fwd-list>
                                    <fwd>{int}</fwd>
                                    <interface-next-hop>
                                            <ip-address>{hop}</ip-address>
                                    </interface-next-hop>
                                </fwd-list>
                            </ip-route-interface-forwarding-list>    
                        </route>
                    </ip>
                </native>
            </config>
            '''
            ip_route_config = netconf_filter.format(
                ip=destination, mask=subnet_mask, int=interface, hop=next_hop
            )
            response = connection.edit_config(ip_route_config, target="running")
            # print(mini.parseString(response.xml).toprettyxml())
            ip_route = xmltodict.parse(response.xml)
            print(json.dumps(ip_route, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def delete_ip_route(destination, subnet_mask, next_hop, interface):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <route>
                            <ip-route-interface-forwarding-list operation="delete">
                                <prefix>{ip}</prefix>
                                <mask>{mask}</mask>
                                <fwd-list>
                                    <fwd>{int}</fwd>
                                    <interface-next-hop>
                                            <ip-address>{hop}</ip-address>
                                    </interface-next-hop>
                                </fwd-list>
                            </ip-route-interface-forwarding-list>    
                        </route>
                    </ip>
                </native>
            </config>
            '''
            ip_route_config = netconf_filter.format(
                ip=destination, mask=subnet_mask, int=interface, hop=next_hop
            )
            response = connection.edit_config(ip_route_config, target="running")
            # print(mini.parseString(response.xml).toprettyxml())
            ip_route = xmltodict.parse(response.xml)
            print(json.dumps(ip_route, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_ip_ssh():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <ssh/>
                    </ip>
                </native>
            </filter>
            '''
            response = connection.get_config("running", netconf_filter)
            print(mini.parseString(response.xml).toprettyxml())
            ip_ssh = xmltodict.parse(response.xml)
            print(json.dumps(ip_ssh, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def get_ip_access_list_standard():
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <filter>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <access-list/>
                    </ip>
                </native>
            </filter>
            '''
            response = connection.get_config("running", netconf_filter)
            print(mini.parseString(response.xml).toprettyxml())
            access_list = xmltodict.parse(response.xml)
            print(json.dumps(access_list, indent=2, sort_keys=True))
            return access_list 
    except Exception as e:
        print(e)


def edit_ip_access_list_standard(name, permit_or_deny, sequence_number, ip_address, wildcard_bits):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <access-list>
                            <standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
                                <name>{id}</name>
                                <access-list-seq-rule>
                                    <sequence>{seq}</sequence>
                                    <{action}>
                                        <std-ace>
                                            <ipv4-prefix>{ip}</ipv4-prefix>
                                            <mask>{mask}</mask>
                                        </std-ace>
                                    </{action}>
                                </access-list-seq-rule>
                            </standard>                                
                        </access-list>        
                    </ip>
                </native>
            </config>
            '''
            access_list_config = netconf_filter.format(
                id=name, seq=sequence_number, action=permit_or_deny, ip=ip_address,
                mask=wildcard_bits
            )
            response = connection.edit_config(access_list_config, target="running")
            # print(mini.parseString(response.xml).toprettyxml())
            access_list = xmltodict.parse(response.xml)
            print(json.dumps(access_list, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


def delete_ip_access_list_standard(name, permit_or_deny, sequence_number, ip_address, wildcard_bits):
    try:
        with manager.connect(
            host=host, 
            port=port, 
            username=user, 
            password=password,
            hostkey_verify=False
        ) as connection:
            netconf_filter = '''
            <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <ip>
                        <access-list>
                            <standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl" operation="delete">
                                <name>{id}</name>
                                <access-list-seq-rule>
                                    <sequence>{seq}</sequence>
                                    <{action}>
                                        <std-ace>
                                            <ipv4-prefix>{ip}</ipv4-prefix>
                                            <mask>{mask}</mask>
                                        </std-ace>
                                    </{action}>
                                </access-list-seq-rule>
                            </standard>                                
                        </access-list>        
                    </ip>
                </native>
            </config>
            '''
            access_list_config = netconf_filter.format(
                id=name, seq=sequence_number, action=permit_or_deny, ip=ip_address,
                mask=wildcard_bits
            )
            response = connection.edit_config(access_list_config, target="running")
            # print(mini.parseString(response.xml).toprettyxml())
            access_list = xmltodict.parse(response.xml)
            print(json.dumps(access_list, indent=2, sort_keys=True))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # edit_int()
    # get_interface_stats("GigabitEthernet3")
    # get_running_config()
    # get_startup_config()
    # get_routing_info()
    # edit_ospf("23", "11.11.11.11", "0.0.0.0", "32", "32.32.32.32")
    # delete_ospf("23", "11.11.11.11", "0.0.0.0", "32", "32.32.32.32")
    # get_ospf_info()
    # get_bgp_info()
    get_capablities()
    # edit_user("aaaaa", "bbbbb", "12")
    # delete_user("aaaaa", "bbbbb", "12")
    # get_users()
    # get_crypto()
    # edit_ip_route("100.100.100.100", "255.255.255.255", "10.1.1.1", "GigabitEthernet2")
    # delete_ip_route("100.100.100.100", "255.255.255.255", "10.1.1.1", "GigabitEthernet2")
    # get_ip_route()
    # get_ip_ssh()
    # edit_ip_access_list_standard("myacl", 'deny', '5', '56.45.56.45', '0.0.0.0')
    # delete_ip_access_list_standard("myacl", 'deny', '5', '56.45.56.45', '0.0.0.0')
    # get_ip_access_list_standard()