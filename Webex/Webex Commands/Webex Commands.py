import requests
import json
import urllib3
from flask import Flask, request
import netmiko
from datetime import datetime
import labenv
from Initial import Handler
import commands

conn = Handler('Webex Commands')
conn.create_room()
conn.webhooks_register()
# conn.delete_webhooks()


app = Flask(__name__)
@app.route('/', methods=["POST"])
def index():
    content = request.get_json()
    message_id = content['data']['id']
    message = conn.actual_message_parse(messageId=message_id)
    message_parsed = message[0:4:1]
    # print(message_parsed)

    if message_parsed == 'Bot:':
        import sys
        sys.exit()
        return content

    else:

        if ":" and ";" not in message:
            conn.post_message("Bot: Invalid syntax. Example syntax: priv: ping 8.8.8.8; asa")

        elif message[0:6:1] == 'priv: ' or message[0:6:1] == 'Priv: ':
            try:
                start_of_message = message[0:6:1]
                new_message = message.replace(start_of_message, '')
                counter = 0
                for c in new_message:
                    if c == ';':
                        seperator = counter
                    counter = counter + 1

                priv_command = new_message[0:seperator:1]
                devices = new_message.replace(f"{priv_command}; ", "")

                list_of_devices = []
                for c in devices:
                    

                    ### FOR ALL DEVICES ###
                    if c != ',' and 'all' in devices:
                        if devices == 'all':
                            commands.priv_command(priv_command, 'all')

                        elif not ',' in devices and devices != 'all':
                            commands.priv_command(priv_command, devices)


                    ### FOR ALL DEVICES AND SOME OTHER DEVICES ERROR ###    
                    elif ',' in devices and 'all' in devices:
                        conn.post_message("Bot: Enter 'all' or device hostnames")
                        break


                    ### FOR A LIST OF DEVICES ###
                    elif ',' in devices and not 'all' in devices:
                        devices = devices.replace(" ", "")
                        list_of_devices = devices.split(',')
                        commands.priv_command(priv_command, list_of_devices)
                        break


                    ### FOR A SINGLE DEVICE ###
                    elif ',' not in devices and 'all' not in devices:
                        devices = devices.replace(" ", "")
                        list_of_devices = devices.split(',')
                        commands.priv_command(priv_command, list_of_devices)
                        break
                
            except Exception as e:
                print(e)

        elif message[0:6:1] == 'conf: ' or message[0:6:1] == 'Conf: ':
            try:

                ### PARSE ALL COMMANDS

                list_of_comms = []
                start_of_message = message[0:6:1]
                new_message = message.replace(start_of_message, '')
                counter = 0

                ## PARSE THE ACTUAL COMMANDS ##
                for c in new_message:
                    if c == ';':
                        seperator = counter
                    counter = counter + 1

                comm_command = new_message[0:seperator:1]
                
                
                for c in comm_command:
                    # PARSE MULTIPLE COMMANDS #
                    if ',' in comm_command:
                        list_of_comms = comm_command.split(',')

                    # PARSE ONE COMMAND #
                    else:
                        temp = new_message.replace(f"{comm_command}; ", "")
                        comms = new_message.replace(f"; {temp}", "")
                        list_of_comms = comms.split(',')
                
                        break

                

                
                ### PARSE ALL DEVICES ###
                start_of_message = message[0:6:1]
                new_message = message.replace(start_of_message, '')
                counter = 0
                for c in new_message:
                    if c == ';':
                        seperator = counter
                    counter = counter + 1

                priv_command = new_message[0:seperator:1]
                devices = new_message.replace(f"{priv_command}; ", "")

                list_of_devices = []
                for c in devices:
                
                    ### FOR ALL DEVICES ###
                    if c != ',' and 'all' in devices:
                        if devices == 'all':
                            commands.conf_command(list_of_comms, 'all')
                            

                        elif not ',' in devices and devices != 'all':
                            commands.conf_command(list_of_comms, devices)
                            

                    ### FOR ALL DEVICES AND SOME OTHER DEVICES ERROR ###    
                    elif ',' in devices and 'all' in devices:
                        conn.post_message("Bot: Enter 'all' or device hostnames")
                        break


                    ### FOR A LIST OF DEVICES ###
                    elif ',' in devices and not 'all' in devices:
                        devices = devices.replace(" ", "")
                        list_of_devices = devices.split(',')
                        commands.conf_command(list_of_comms, list_of_devices)
                        break


                    ### FOR A SINGLE DEVICE ###
                    elif ',' not in devices and 'all' not in devices:
                        devices = devices.replace(" ", "")
                        list_of_devices = devices.split(',')
                        commands.conf_command(list_of_comms, list_of_devices)
                        break
                
            except Exception as e:
                print(e)

        elif message == 'cancel':
            import sys
            sys.exit()
            return content

        else:
            conn.post_message("Bot: Enter a valid command")
    return content

if __name__ == '__main__':
    app.run(debug=True, port=8000)