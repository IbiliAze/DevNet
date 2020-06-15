import netmiko
import labenv
from datetime import datetime
import os
import json
import smtplib

time = (datetime.now()).date()


def backup():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                print(f"Backing up {device['hostname']}")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                back_up = 'show run'
                running_config = connection.send_command(back_up)
                backup_file = open(f"backup {ip} {time}.txt", "w")
                backup_file.write(running_config)
                print(f" -{device['hostname']} has been backed up")
                print()
            except Exception as e:
                print(f"Connection to {device['hostname']} has failed")
                print(f" -Exception: {e}")
                print()

        elif device['type'] == 'firewall':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            secret = device['secret']
            try:
                print(f"Backing up {device['hostname']}")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_asa",
                    username=user, password=pw, secret=secret)
                back_up = 'show run'
                running_config = connection.send_command(back_up)
                backup_file = open(f"backup {ip} {time}.txt", "w")
                backup_file.write(running_config)
                print(f" -{device['hostname']} has been backed up")
                print()
            except Exception as e:
                print(f"Connection to {device['hostname']} has failed")
                print(f" -Exception: {e}")
                print()

        elif device['type'] == 'cisco_xe':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            port = device['port']
            try:
                print(f"Backing up {device['hostname']}")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_xe",
                    username=user, password=pw, port=port)
                back_up = 'show run'
                running_config = connection.send_command(back_up)
                backup_file = open(f"backup {ip} {time}.txt", "w")
                backup_file.write(running_config)
                print(f" -{device['hostname']} has been backed up")
                print()
            except Exception as e:
                print(f"Connection to {device['hostname']} has failed")
                print(f" -Exception: {e}")
                print()


def add_users():
    users = str(input("Enter a Username: "))
    passwords = str(input(f"Enter a Password for {users}: "))
    privilege_level = str(input(f"Enter a Privilege Level for {users}: "))
    
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                print(f"Adding users to {device['hostname']}...")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                users_commands = [f'username {users} privil {privilege_level} password {passwords}']
                connection.send_config_set(users_commands)
                print(f"User {users} have been added to {device['hostname']}.")
                print()
            except Exception as e:
                print(e)
                print()

        elif device['type'] == 'firewall':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            secret = device['secret']
            try:
                print(f"Adding users to {device['hostname']}...")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_asa",
                    username=user, password=pw, secret=secret)
                users_commands = [f'username {users} password {passwords} privil {privilege_level}']
                connection.send_config_set(users_commands)
                print(f"User {users} have been added to {device['hostname']}.")
                print()
            except Exception as e:
                print(e)
                print()

        elif device['type'] == 'cisco_xe':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            port = device['port']
            try:
                print(f"Adding users to {device['hostname']}...")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_xe",
                    username=user, password=pw, port=port)
                users_commands = [f'username {users} privil {privilege_level} password {passwords}']
                connection.send_config_set(users_commands)
                print(f"User {users} have been added to {device['hostname']}.")
                print()
            except Exception as e:
                print(e)
                print()


def internet_reachability():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                print(f"Testing {device['hostname']}'s Internet reachability")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                users_commands = 'ping 8.8.8.8'
                print(connection.send_command(users_commands))
                print()
            except Exception as e:
                print(e)
                print()
        elif device['type'] == 'firewall':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            secret = device['secret']
            try:
                print(f"Testing {device['hostname']}'s Internet reachability'")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_asa",
                    username=user, password=pw, secret=secret)
                users_commands = 'ping 8.8.8.8'
                print(connection.send_command(users_commands))
                print()
            except Exception as e:
                print(e)
                print()        


def dmvpn():
    dmvpn_network_id = str(input("Enter the NHRP Network-ID: "))
    dmvpn_authentication = str(input("Enter the NHRP Authentication Token: "))
    tunnel_key = str(input("Enter the Tunnel Key: "))
    isakmp_key = str(input("Enter the crypto ISAKMP key: "))
    counter = 1
    for device in labenv.devices:
        if device['type'] == 'ios' and device['hostname'] == 'r1':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                tunnel_ip_address = str(input("Enter the Hub Tunnel interface IP address: "))
                tunnel_subnet_mask = str(input("Enter the Hub Tunnel interface Subnet Mask: "))
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                crypto_commands = [f"crypto isakmp key 0 {isakmp_key} address 0.0.0.0", 
                    "crypto isakmp policy 1", "authentication pre-share", "encryption aes 256",
                    "hash md5", "group 5", "lifetime 70000",
                    "crypto ipsec transform-set Tset esp-aes 256 esp-md5-hmac",
                    "crypto ipsec profile IPSEC-PROFILE", "set transform-set Tset"]
                tunnel_commands = [f"interface tunnel 100", 
                    f"ip address {tunnel_ip_address} {tunnel_subnet_mask}",
                    f"ip nhrp network-id {dmvpn_network_id}", 
                    f"ip nhrp authentication {dmvpn_authentication}",
                    f"tunnel key {tunnel_key}", "ip nhrp redirect", "ip nhrp shortcut",
                    "ip nhrp map multicast dynamic", "tunnel protection ipsec profile IPSEC-PROFILE",
                    "tunnel mode gre multipoint", "tunnel source gig0/0",
                    "ip mtu 1400", "ip tcp adjust-mss 1360", "no shut"]
                eigrp_ospf_commands = ["router ospf 1", f"network {ip} 0.0.0.0 area 0",
                    "router eigrp 100", f"network {tunnel_ip_address} 0.0.0.0", "no auto"]
                print(f"Configuring the Hub {device['hostname']}...")
                connection.send_config_set(crypto_commands, tunnel_commands, eigrp_ospf_commands)
                print()
            except Exception as e:
                print(e)
                print()
        elif device['type'] == 'ios' and device['hostname'] != 'r1':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                tunnel_ip_address = str(input(f"Enter the {device['hostname']} Tunnel interface IP address: "))
                tunnel_subnet_mask = str(input(f"Enter the {device['hostname']} Tunnel interface Subnet Mask: "))
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                crypto_commands = [f"crypto isakmp key 0 {isakmp_key} address 0.0.0.0", 
                    "crypto isakmp policy 1", "authentication pre-share", "encryption aes 256",
                    "hash md5", "group 5", "lifetime 70000",
                    "crypto ipsec transform-set Tset esp-aes 256 esp-md5-hmac",
                    "crypto ipsec profile IPSEC-PROFILE", "set transform-set Tset"]
                tunnel_commands = [f"interface tunnel 100", 
                    f"ip address {tunnel_ip_address} {tunnel_subnet_mask}",
                    f"ip nhrp network-id {dmvpn_network_id}", 
                    f"ip nhrp authentication {dmvpn_authentication}",
                    f"tunnel key {tunnel_key}", "ip nhrp redirect", "ip nhrp shortcut",
                    f"ip nhrp map {tunnel_ip_address} {ip}",
                    f"ip nhrp nhs {tunnel_ip_address}",
                    f"ip nhrp map multicast {ip}", "tunnel protection ipsec profile IPSEC-PROFILE",
                    "tunnel mode gre multipoint", "tunnel source gig0/0",
                    "ip mtu 1400", "ip tcp adjust-mss 1360", "no shut"]
                eigrp_ospf_commands = ["router ospf 1", f"network {ip} 0.0.0.0 area 0",
                    "router eigrp 100", f"network {tunnel_ip_address} 0.0.0.0", "no auto"]
                print(f"Configuring the Spoke {counter} {device['hostname']}...")
                connection.send_config_set(crypto_commands, tunnel_commands, eigrp_ospf_commands)
                counter =+ 1
                print()
            except Exception as e:
                print(e)
                print()


def ntp():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                print(f"Configuring NTP on {device['hostname']}")
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                ntp_commands = ['ntp server 132.163.96.5']
                ntp = connection.send_config_set(ntp_commands)
                print(f" -{device['hostname']} has been configured")
                print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_ip_interface_brief():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                interfaces = connection.send_command('show ip int brief', use_textfsm=True)
                # print(json.dumps(interfaces, indent=2, sort_keys=True))
                for interface in interfaces:
                    print(f"Interface: {interface['intf']}")
                    print(f" -IP Address: {interface['ipaddr']}")
                    print(f"  -Link: {interface['status']}")
                    print(f"   -Line Protocol: {interface['proto']}")
                    print()
                print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()
        if device['type'] == 'firewall':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            secret = device['secret']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_asa",
                    username=user, password=pw, secret=secret)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                interfaces = connection.send_command('show interface', use_textfsm=True)
                # print(json.dumps(interfaces, indent=2, sort_keys=True))
                for interface in interfaces:
                    print(f"Interface: {interface['interface']}")
                    print(f" -Zone: {interface['interface_zone']}")
                    print(f"  -IP Address: {interface['ip_address']} {interface['net_mask']}")
                    print(f"   -MAC Address: {interface['address']}")
                    print(f"    -Link: {interface['link_status']}")
                    print(f"     -Line Protocol: {interface['protocol_status']}")
                    print(f"      -Bandwidth: {interface['bandwidth']}")
                    print()
                print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_ip_ospf_neighbnors_ios():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                ospf_neighbors = connection.send_command('show ip ospf neigh', use_textfsm=True)
                # print(json.dumps(ospf_neighbors, indent=2, sort_keys=True))
                for neighbor in ospf_neighbors:
                    print(f"Neighbor: {neighbor['address']} with a RID of {neighbor['neighbor_id']}")
                    print(f" -State: {neighbor['state']}")
                    print(f"  -Interface: {neighbor['interface']}")
                    print(f"   -Priority: {neighbor['priority']}")
                    print(f"    -Dead-Time: {neighbor['dead_time']}")
                    print()
                    print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_ip_eigrp_neighbors_ios():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                ospf_neighbors = connection.send_command('show ip eigrp neigh', use_textfsm=True)
                # print(json.dumps(ospf_neighbors, indent=2, sort_keys=True))
                for neighbor in ospf_neighbors:
                    print(f"Neighbor: {neighbor['address']} on AS {neighbor['as']}")
                    print(f" -Hold-Down Timer: {neighbor['hold']}")
                    print(f"  -Interface: {neighbor['interface']}")
                    print(f"   -Uptime: {neighbor['uptime']}")
                    print()
                    print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_cdp_neighbors_ios():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                cdp = connection.send_command('show cdp neighbors', use_textfsm=True)
                print(json.dumps(cdp, indent=2, sort_keys=True))
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_clock_ios():
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                clock_json = connection.send_command('show clock', use_textfsm=True)
                clock = clock_json[0]
                print(f"{clock['timezone']} {clock['dayweek']} {clock['day']}-{clock['month']}-{clock['year']}")
                # print(json.dumps(clock, indent=2, sort_keys=True))
                print()
                print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_nat_asa():
    for device in labenv.devices:
        if device['type'] == 'firewall':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            secret = device['secret']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_asa",
                    username=user, password=pw, secret=secret)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                nats = connection.send_command('show nat', use_textfsm=True)
                # print(json.dumps(nats, indent=2, sort_keys=True))
                for nat in nats:
                    print(f"Line Number: {nat['line_number']}")
                    print(f"Source Interface: {nat['source_interface']}")
                    print(f"Destination Interface: {nat['destination_interface']}")
                    print(f" -Source Type: {nat['source_type']}")
                    print(f"  -Hits: {nat['translate_hits']}")
                    print(f"  -Reverse-Hits: {nat['untranslate_hits']}")
                    if nat['destination_mapped'] == '':
                        print("    -Destination/Twice NAT is NOT Enabled")
                    else:
                        print("    -Destination/Twice NAT is Enabled")
                    print()
                    print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_ios(show_command):
    for device in labenv.devices:
        if device['type'] == 'ios':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_ios",
                    username=user, password=pw)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                output = connection.send_command(show_command)
                print(json.dumps(output, indent=2, sort_keys=True))
                print()
                print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def show_asa(show_command):
    for device in labenv.devices:
        if device['type'] == 'firewall':
            ip = device['ip']
            user = device['user']
            pw = device['pw']
            secret = device['secret']
            try:
                connection = netmiko.ConnectHandler(ip=ip, device_type="cisco_asa",
                    username=user, password=pw, secret=secret)
                connection.enable()
                print(f"Device {device['hostname']}")
                print("-" * 20)
                output = connection.send_command(show_command)
                print(json.dumps(output, indent=2, sort_keys=True))
                print()
                print()
            except Exception as e:
                print(f" -Exception: {e}")
                print()


def reach_from_your_node():
    pass


def send_email():
    try:
        sender_email = ""
        receiver_email = ""
        password = ""
        message = "hey, this was send through python :O"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user=sender_email, password=password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent")
    except Exception as e:
        print(f" -Exception: {e}")
        print()




if  __name__ == "__main__":  
    # send_email() 
    # show_ios("show crypto isa sa")
    # show_asa("sho ospf nei")
    # backup()
    dmvpn()