import requests
import json 
import urllib3
from flask import Flask, request
import netmiko
from datetime import datetime
from labenv import devices
from Initial import Handler


def priv_command(command, devices_list):
    conn = Handler('Webex Commands')
    time = (datetime.now()).date()



    if devices_list == 'all':
        for device in devices:

            if device['type'] == 'cisco_xe':
                iosxe_connection_params = {
                    'ip': device['ip'],
                    'device_type': 'cisco_xe',
                    'username': device['user'],
                    'password': device['pw'],
                    'port': device['port']
                }
                try:
                    print(f"Connecting to {device['hostname']}")
                    conn.post_message(f"Bot: connecting to {device['hostname']}")
                    connection = netmiko.ConnectHandler(**iosxe_connection_params)
                    print(f"Running '{command}' on {device['hostname']}")
                    conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                    send_command = connection.send_command(command)
                    print(f"Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: {send_command}")
                except Exception as e:
                    print(f"Connection to {device['hostname']} has failed")
                    print(f" -Exception: {e}")
                    print()
                    conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

            elif device['type'] == 'cisco_ios':
                ios_connection_params = {
                    'ip': device['ip'],
                    'device_type': 'cisco_ios',
                    'username': device['user'],
                    'password': device['pw']
                }
                try:
                    print(f"Connecting to {device['hostname']}")
                    conn.post_message(f"Bot: connecting to {device['hostname']}")
                    connection = netmiko.ConnectHandler(**ios_connection_params)
                    print(f"Running '{command}' on {device['hostname']}")
                    conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                    send_command = connection.send_command(command)
                    print(f"Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: {send_command}")
                except Exception as e:
                    print(f"Connection to {device['hostname']} has failed")
                    print(f" -Exception: {e}")
                    print()
                    conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

            elif device['type'] == 'cisco_asa':
                asa_connection_params = {
                    'ip': device['ip'],
                    'device_type': 'cisco_asa',
                    'username': device['user'],
                    'password': device['pw'],
                    'secret': device['secret']
                }
                try:
                    print(f"Connecting to {device['hostname']}")
                    conn.post_message(f"Bot: connecting to {device['hostname']}")
                    connection = netmiko.ConnectHandler(**asa_connection_params)
                    print(f"Running '{command}' on {device['hostname']}")
                    conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                    send_command = connection.send_command(command)
                    print(f"Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: {send_command}")
                except Exception as e:
                    print(f"Connection to {device['hostname']} has failed")
                    print(f" -Exception: {e}")
                    print()
                    conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

            


    elif type(devices_list) == list:
        for device in devices:
            if device['hostname'] in devices_list:

                if device['type'] == 'cisco_xe':
                    iosxe_connection_params = {
                        'ip': device['ip'],
                        'device_type': 'cisco_xe',
                        'username': device['user'],
                        'password': device['pw'],
                        'port': device['port']
                    }
                    try:
                        print(f"Connecting to {device['hostname']}")
                        conn.post_message(f"Bot: connecting to {device['hostname']}")
                        connection = netmiko.ConnectHandler(**iosxe_connection_params)
                        print(f"Running '{command}' on {device['hostname']}")
                        conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                        send_command = connection.send_command(command)
                        print(f"Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: {send_command}")
                    except Exception as e:
                        print(f"Connection to {device['hostname']} has failed")
                        print(f" -Exception: {e}")
                        print()
                        conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

                elif device['type'] == 'cisco_ios':
                    ios_connection_params = {
                        'ip': device['ip'],
                        'device_type': 'cisco_ios',
                        'username': device['user'],
                        'password': device['pw']
                    }
                    try:
                        print(f"Connecting to {device['hostname']}")
                        conn.post_message(f"Bot: connecting to {device['hostname']}")
                        connection = netmiko.ConnectHandler(**ios_connection_params)
                        print(f"Running '{command}' on {device['hostname']}")
                        conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                        send_command = connection.send_command(command)
                        print(f"Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: {send_command}")
                    except Exception as e:
                        print(f"Connection to {device['hostname']} has failed")
                        print(f" -Exception: {e}")
                        print()
                        conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

                elif device['type'] == 'cisco_asa':
                    asa_connection_params = {
                        'ip': device['ip'],
                        'device_type': 'cisco_asa',
                        'username': device['user'],
                        'password': device['pw'],
                        'secret': device['secret']
                    }
                    try:
                        print(f"Connecting to {device['hostname']}")
                        conn.post_message(f"Bot: connecting to {device['hostname']}")
                        connection = netmiko.ConnectHandler(**asa_connection_params)
                        print(f"Running '{command}' on {device['hostname']}")
                        conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                        send_command = connection.send_command(command)
                        print(f"Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: {send_command}")
                    except Exception as e:
                        print(f"Connection to {device['hostname']} has failed")
                        print(f" -Exception: {e}")
                        print()
                        conn.post_message(f"Bot: Connection to {device['hostname']} has failed")





def conf_command(command, devices_list):
    conn = Handler('Webex Commands')
    time = (datetime.now()).date()

    if devices_list == 'all':
        for device in devices:

            if device['type'] == 'cisco_xe':
                iosxe_connection_params = {
                    'ip': device['ip'],
                    'device_type': 'cisco_xe',
                    'username': device['user'],
                    'password': device['pw'],
                    'port': device['port']
                }
                try:
                    print(f"Connecting to {device['hostname']}")
                    conn.post_message(f"Bot: connecting to {device['hostname']}")
                    connection = netmiko.ConnectHandler(**iosxe_connection_params)
                    print(f"Running '{command}' on {device['hostname']}")
                    conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                    send_command = connection.send_config_set(command)
                    print(f"Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: {send_command}")
                except Exception as e:
                    print(f"Connection to {device['hostname']} has failed")
                    print(f" -Exception: {e}")
                    print()
                    conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

            elif device['type'] == 'cisco_ios':
                ios_connection_params = {
                    'ip': device['ip'],
                    'device_type': 'cisco_ios',
                    'username': device['user'],
                    'password': device['pw']
                }
                try:
                    print(f"Connecting to {device['hostname']}")
                    conn.post_message(f"Bot: connecting to {device['hostname']}")
                    connection = netmiko.ConnectHandler(**ios_connection_params)
                    print(f"Running '{command}' on {device['hostname']}")
                    conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                    send_command = connection.send_config_set(command)
                    print(f"Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: {send_command}")
                except Exception as e:
                    print(f"Connection to {device['hostname']} has failed")
                    print(f" -Exception: {e}")
                    print()
                    conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

            elif device['type'] == 'cisco_asa':
                asa_connection_params = {
                    'ip': device['ip'],
                    'device_type': 'cisco_asa',
                    'username': device['user'],
                    'password': device['pw'],
                    'secret': device['secret']
                }
                try:
                    print(f"Connecting to {device['hostname']}")
                    conn.post_message(f"Bot: connecting to {device['hostname']}")
                    connection = netmiko.ConnectHandler(**asa_connection_params)
                    print(f"Running '{command}' on {device['hostname']}")
                    conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                    send_command = connection.send_config_set(command)
                    print(f"Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                    conn.post_message(f"Bot: {send_command}")
                except Exception as e:
                    print(f"Connection to {device['hostname']} has failed")
                    print(f" -Exception: {e}")
                    print()
                    conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

                    
      


    elif type(devices_list) == list:
        for device in devices:
            if device['hostname'] in devices_list:

                if device['type'] == 'cisco_xe':
                    iosxe_connection_params = {
                        'ip': device['ip'],
                        'device_type': 'cisco_xe',
                        'username': device['user'],
                        'password': device['pw'],
                        'port': device['port']
                    }
                    try:
                        print(f"Connecting to {device['hostname']}")
                        conn.post_message(f"Bot: connecting to {device['hostname']}")
                        connection = netmiko.ConnectHandler(**iosxe_connection_params)
                        print(f"Running '{command}' on {device['hostname']}")
                        conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                        send_command = connection.send_config_set(command)
                        print(f"Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: {send_command}")
                    except Exception as e:
                        print(f"Connection to {device['hostname']} has failed")
                        print(f" -Exception: {e}")
                        print()
                        conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

                elif device['type'] == 'cisco_ios':
                    ios_connection_params = {
                        'ip': device['ip'],
                        'device_type': 'cisco_ios',
                        'username': device['user'],
                        'password': device['pw']
                    }
                    try:
                        print(f"Connecting to {device['hostname']}")
                        conn.post_message(f"Bot: connecting to {device['hostname']}")
                        connection = netmiko.ConnectHandler(**ios_connection_params)
                        print(f"Running '{command}' on {device['hostname']}")
                        conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                        send_command = connection.send_config_set(command)
                        print(f"Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: {send_command}")
                    except Exception as e:
                        print(f"Connection to {device['hostname']} has failed")
                        print(f" -Exception: {e}")
                        print()
                        conn.post_message(f"Bot: Connection to {device['hostname']} has failed")

                elif device['type'] == 'cisco_asa':
                    asa_connection_params = {
                        'ip': device['ip'],
                        'device_type': 'cisco_asa',
                        'username': device['user'],
                        'password': device['pw'],
                        'secret': device['secret']
                    }
                    try:
                        print(f"Connecting to {device['hostname']}")
                        conn.post_message(f"Bot: connecting to {device['hostname']}")
                        connection = netmiko.ConnectHandler(**asa_connection_params)
                        print(f"Running '{command}' on {device['hostname']}")
                        conn.post_message(f"Bot: Running '{command}' on {device['hostname']}")
                        send_command = connection.send_config_set(command)
                        print(f"Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: Command '{command}' has been sent to {device['hostname']}")
                        conn.post_message(f"Bot: {send_command}")
                    except Exception as e:
                        print(f"Connection to {device['hostname']} has failed")
                        print(f" -Exception: {e}")
                        print()
                        conn.post_message(f"Bot: Connection to {device['hostname']} has failed")
                        