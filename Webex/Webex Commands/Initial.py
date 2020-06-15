import requests
import json 
import urllib3
from flask import Flask, request
import netmiko
from datetime import datetime
import labenv
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ngrok_URL = 'http://5a47aa18.ngrok.io'

webex_token = 'Bearer Yjg3ZTEzYTgtMDZlMS00MWVhLTg4YWItNmVhODY2MjZmMjYxM2NmZTY4ZTYtMmY0_PF84_bdc9a8b4-40e0-44a7-96eb-5e6cea4788dd'
path = '/rooms'
url = f'https://api.ciscospark.com/v1{path}'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': webex_token
}



class Handler:


    def __init__(self, room_name):
        self.room_name = room_name


    def create_room(self):
        teams_url = 'https://api.ciscospark.com/v1/teams'
        rooms_url = "https://api.ciscospark.com/v1/rooms"
        teamId = ''
        roomId = ''
        teams_body = {
            "name": f"{self.room_name} Team"
        }
        rooms_body = {
            "title": self.room_name,
            "teamId": teamId
        }
        try:
            get_teams = requests.get(teams_url, headers=headers, verify=False).json()
            get_rooms = requests.get(rooms_url, headers=headers, verify=False).json()
            for team in get_teams['items']:
                if team['name'] == f"{self.room_name} Team":
                    teamId = team['id']
                    get_rooms = requests.get(rooms_url, headers=headers, verify=False).json()
                    for room in get_rooms['items']:
                        if room['title'] == self.room_name:
                            roomId = room['id']
                            return roomId
                        break
                else:
                    post_teams = requests.post(teams_url, headers=headers, verify=False,
                        data=json.dumps(teams_body)).json()
                    get_teams = requests.get(teams_url, headers=headers, verify=False).json()
                    for team in get_teams['items']:
                        if team['name'] == f"{self.room_name} Team":
                            teamId = team['id']
                    rooms_body = {
                        "title": self.room_name,
                        "teamId": teamId
                    }
                    post_rooms = requests.post(rooms_url, headers=headers, verify=False,
                        data=json.dumps(rooms_body)).json()
                    get_rooms = requests.get(rooms_url, headers=headers, verify=False).json()
                    for room in get_rooms['items']:
                        if room['title'] == self.room_name:
                            roomId = room['id']
                            return roomId
        except Exception as e:
            print(e)


    def webhooks_register(self):
        try:
            path = '/webhooks'
            url = f'https://api.ciscospark.com/v1{path}'
            get_webhook = requests.get(url, headers=headers, verify=False).json()
            # print(json.dumps(get_webhook, indent=2, sort_keys=True))

            if len(get_webhook['items']) == 0:
                print('Creating a new webhook')
                payload = {
                    "resource" : "messages",
                    "event" : "created",
                    "filter" : f"roomId={self.create_room()}",
                    "targetUrl" : f"{ngrok_URL}",
                    "name" : "WebEx Team Learning Lab Webhook"
                }          
                post_webhook = requests.post(url, headers=headers, verify=False,
                    data=json.dumps(payload)).json()
                get_webhook = requests.get(url, headers=headers, verify=False).json()
                # print(json.dumps(get_webhook, indent=2, sort_keys=True))
                return get_webhook['id']

            else: 
                for webhook in get_webhook['items']:

                    if webhook['filter'] == f"roomId={self.create_room()}":
                        print("The webhook has already been registered")
                        return

                    else:
                        print('Creating a new webhook')
                        payload = {
                            "resource" : "messages",
                            "event" : "created",
                            "filter" : f"roomId={self.create_room()}",
                            "targetUrl" : f"{ngrok_URL}",
                            "name" : "WebEx Team Learning Lab Webhook"
                        }          
                        post_webhook = requests.post(url, headers=headers, verify=False,
                            data=json.dumps(payload)).json()
                        get_webhook = requests.get(url, headers=headers, verify=False).json()
                        # print(json.dumps(get_webhook, indent=2, sort_keys=True))
           
        except Exception as e:
            print(e)


    def delete_webhooks(self):
        try:
            path = '/webhooks'
            url = f'https://api.ciscospark.com/v1{path}'
            get_webhook = requests.get(url, headers=headers, verify=False).json()
            for webhook in get_webhook['items']:
                webhookId = webhook['id']
                path = f'/webhooks/{webhookId}'
                url = f'https://api.ciscospark.com/v1{path}'
                delete_webhook = requests.delete(url, headers=headers, verify=False)
            
            path = '/webhooks'
            url = f'https://api.ciscospark.com/v1{path}'
            get_webhook = requests.get(url, headers=headers, verify=False).json()
            print('deleted webhooks')
        except Exception as e:
            print(e)


    def post_message(self, message):
        try:
            url = "https://api.ciscospark.com/v1/messages"
            payload = {
                "roomId": self.create_room(),
                "text": message
            }
            msg_post = requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()
            print("Posted a message")
        except Exception as e:
            print(e)


    def actual_message_parse(self, messageId):
        try:
            message_id = messageId
            path = f'/messages/{message_id}'
            url = f'https://api.ciscospark.com/v1{path}'
            response = requests.get(url, headers=headers, verify=False).json()
            message = response['text']
            return message
        except Exception as e:
            print(e)



