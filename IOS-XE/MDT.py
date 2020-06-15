from ncclient import manager
import xmltodict
import logging
from lxml.etree import fromstring
import json

class IOS_XE:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


    def get_capabilities(self):
        ''' get netconf capabilites '''
        try:
            with manager.connect(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password = self.password,
                    hostkey_verify= False,
                    manager_params ={'timeout':100},
                    device_params= {"name": "csr"}) as connection:
                
                for capability in connection.server_capabilities:
                    print(capability)
        except Exception as ex:
            print(ex)


    def subscribe_mdt_subs(self, period):
        ''' subscribe to mdt subscriptions '''
        try:
            with manager.connect(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password = self.password,
                    hostkey_verify= False,
                    device_params = {'name': 'csr'}) as connection:
                
                sub_endpoints = [
                    "/mdt-oper:mdt-oper-data/mdt-subscriptions"
                ]
                for subscription in sub_endpoints:
                    rpc = f"""
                        <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
                            <stream>yp:yang-push</stream>
                            <yp:xpath-filter>{subscription}</yp:xpath-filter>
                            <yp:period>{period}</yp:period>
                        </establish-subscription>
                    """
                    subscribe = connection.dispatch(fromstring(rpc))
                    response = xmltodict.parse(subscribe.xml)
                    # print(json.dumps(response, indent=2, sort_keys=True))
                    
                    if connection.take_notification():
                        counter = 0
                        while counter < 5:
                            data_xml = connection.take_notification()
                            data = xmltodict.parse(data_xml.notification_xml)
                            counter = counter + 1
                            print(json.dumps(data, indent=2, sort_keys=True))
                            print()
                    else:
                        print("There's no data to display")
                        
        except Exception as ex:
            print(ex)


    def subscribe_cpu_utilisation(self, period):
        ''' subscribe to cpu utilisation '''
        try:
            with manager.connect(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password = self.password,
                    hostkey_verify= False,
                    device_params = {'name': 'csr'}) as connection:
                
                sub_endpoints = [
                    "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization"
                ]
                for subscription in sub_endpoints:
                    rpc = f"""
                        <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
                            <stream>yp:yang-push</stream>
                            <yp:xpath-filter>{subscription}</yp:xpath-filter>
                            <yp:period>{period}</yp:period>
                        </establish-subscription>
                    """
                    subscribe = connection.dispatch(fromstring(rpc))
                    response = xmltodict.parse(subscribe.xml)
                    print(json.dumps(response, indent=2, sort_keys=True))
                    
                    if connection.take_notification():
                        counter = 0
                        while counter < 5:
                            data_xml = connection.take_notification()
                            data = xmltodict.parse(data_xml.notification_xml)
                            counter = counter + 1
                            print(json.dumps(data, indent=2, sort_keys=True))
                            print()
                    else:
                        print("There's no data to display")
                        
        except Exception as ex:
            print(ex)

                

if __name__ == '__main__':
    ios_xe_params_always_on = {
        'host': 'ios-xe-mgmt-latest.cisco.com', 
        'port': '10000', 
        'username': 'developer', 
        'password': 'C1sco12345',
    }
    ios_xe_params_reserved = {
        'host': '10.10.20.48', 
        'port': '830', 
        'username': 'developer', 
        'password': 'C1sco12345',
    }
    r1= {
        'host': '192.168.0.59', 
        'port': '22', 
        'username': 'ibi', 
        'password': 'cisco',
    }


    

    ios_xe = IOS_XE(**ios_xe_params_always_on)
    # ios_xe.get_capabilities()
    ios_xe.subscribe_mdt_subs(500)
    # ios_xe.subscribe_cpu_utilisation(500)
