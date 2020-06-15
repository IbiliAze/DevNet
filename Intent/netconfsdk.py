import xml.dom.minidom as mini
from pprint import pprint
import json
import xmltodict
from ncclient import manager

class netconf:

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password


    def req(self, rpc, data_source, dictionary=True, print_output=True, config=None, filt=None):
        ''' request helper function '''
        try:
            with manager.connect(
                host=self.host, 
                port=self.port, 
                username=self.username, 
                password=self.password, 
                hostley_verify=False) as connection:

                if rpc == 'get':
                    reply = connection.get(filter=filt, source=data_source)
                    reply_xml = mini.parseString(str(reply))
                    reply_pretty_xml = reply_xml.toprettyxml(indent="  ")
                    print(reply_pretty_xml)


        except Exception as ex:
            print(ex)


    def interfaces()


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


    

    ios_xe = netconf(**ios_xe_params_always_on)
    ios_xe.req()