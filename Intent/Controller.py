from MDT_Model import MDT_Model_Tool
import time
import psutil 
import matplotlib.pyplot as plt
import random
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation

class MDT_Controller:

    def __init__(self, host, username, password, port, hostkey_verify):

        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.hostkey_verify = hostkey_verify


    def subscribe_cpu(self, period, PID, sub_metric, debug_lines=False):

        subsctiption = MDT_Model_Tool(host=self.host, username=self.username, 
            password=self.password, port=self.port, hostkey_verify=self.hostkey_verify)
        subsctiption.cpu_usage(period, PID, sub_metric)


    def receive_updates(self, stream_data):
        print(stream_data)

    def plot_graph(self):
        plt.rcParams['animation.html'] = 'jshtml'
        fig = plt.figure()
        ax = fig.add_subplot(111)
        fig.show()



if __name__ == '__main__':
    ios_xe_params_reserved = {
        'host':'ios-xe-mgmt-latest.cisco.com', 
        'username':'developer', 
        'password':'C1sco12345', 
        'port':'10000', 
        'hostkey_verify':False
    }

    subscription = MDT_Controller(**ios_xe_params_reserved)   
    subscription.subscribe_cpu(period=400, PID='LOCAL AAA', sub_metric='invocation-count')