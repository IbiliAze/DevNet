from ncclient import manager
import json
import xmltodict
from pprint import pprint
from lxml.etree import fromstring


class MDT_Model_Tool:

    def __init__(self, host, username, password, port, hostkey_verify):

        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.hostkey_verify = hostkey_verify
        self.rpc = """
                <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
                    <stream>yp:yang-push</stream>
                    <yp:xpath-filter>{}</yp:xpath-filter>
                    <yp:period>{}</yp:period>
                </establish-subscription>
            """


    def cpu_usage(self, period, PID, sub_metric='avg-run-time', model_metric='/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization', debug_lines=False):
        ''' CPU usage MDT YANG Model '''
        try: 
            with manager.connect(
                    host=self.host, 
                    username=self.username, 
                    password=self.password,
                    port=self.port, 
                    hostkey_verify = self.hostkey_verify,
                    device_params = {'name': 'csr'}) as connection:

                subscribe = connection.dispatch(fromstring(self.rpc.format(model_metric, period)))
                response = xmltodict.parse(subscribe.xml)
                if debug_lines == True:
                    print(json.dumps(response, indent=2, sort_keys=True))
                
                if response['rpc-reply']['subscription-result']['#text'] == 'notif-bis:error-insufficient-resources':
                    print(f"Could not subscribe to the resource.\nIssue could reply on the period (It's given in centiseconds, try 500 for 5 seconds) \nError: {response['rpc-reply']['subscription-result']['#text']}")
                    return response
                else:
                    if connection.take_notification():
                        counter = 0
                        while counter < 50:
                            data_xml = connection.take_notification()
                            data = xmltodict.parse(data_xml.notification_xml)
                            sub_datas = data['notification']['push-update']['datastore-contents-xml'] \
                                ['cpu-usage']['cpu-utilization']['cpu-usage-process']
                            for sub_data in sub_datas:
                                if sub_data['name'] == PID:
                                    final_metric = {PID: sub_data[sub_metric]}
                                    from Controller import MDT_Controller
                                    MDT_Controller.receive_updates(self, stream_data=final_metric)
                                    MDT_Controller.plot_graph(self)
                                    if debug_lines == True:
                                        print(data)
                            counter = counter + 1

        except Exception as ex:
            print(ex)