import requests
import json
import urllib3
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token = 'ZmVlYjRhMzUtMGVlZi00NzAxLWJkZDctNGVkNDVmODk0ODQ2NzJjMzA0NTEtM2Vj_PF84_bdc9a8b4-40e0-44a7-96eb-5e6cea4788dd'
 
 #the token is carried in the request header
url = 'https://api.ciscospark.com/v1/teams'
headers = {"Authorization": f"Bearer {token}",
           "Content-Type": "application/json"}

body = {
    "name": "Weather Team"
}

presp = requests.post(url, data=json.dumps(body), headers=headers, verify=False).json()
print(presp)
gresp = requests.get(url, headers=headers, verify=False).json()
print(json.dumps(gresp, indent=2, sort_keys=True))

teams = gresp['items']
for team in teams:
    if team['name'] == 'Weather Team':
        teamId = team['id']

room_url = "https://api.ciscospark.com/v1/rooms"
room_body = {
    "title": "Weather Room",
    "teamId": teamId
}
room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body), verify=False).json()
room_get = requests.get(room_url, headers=headers, verify=False).json()
print(json.dumps(room_get, indent=2, sort_keys=True))

for room in room_get['items']:
    if room['title'] == "Weather Room":
        roomId = room['id']
        

msg_url = "https://api.ciscospark.com/v1/messages"
msg_body = {
    "roomId": roomId,
    "text": "suiiii wazap cunts"
}
msg_post = requests.post(msg_url, headers=headers, data=json.dumps(msg_body), verify=False).json()



print(roomId)