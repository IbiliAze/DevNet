import urllib3
import json
import requests
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'https://api.ciscospark.com'
teams_path = "/v1/teams"
rooms_path = "/v1/rooms"
msg_path = "/v1/messages"
token = "Bearer ODk2NTg5YjUtNjU2OC00M2YxLWIyNjEtZmYzNjFjNjk0NzIyYTI0ODEwODgtZGRl_PF84_bdc9a8b4-40e0-44a7-96eb-5e6cea4788dd"

teams_url = f"{host}{teams_path}"
rooms_url = f"{host}{rooms_path}"
msg_url = f"{host}{msg_path}"

teams_body = {
    "name": "Our Main Team"
}

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

teams_post = requests.post(teams_url, headers=headers, data=json.dumps(teams_body), verify=False).json()
teams_get = requests.get(teams_url, headers=headers, verify=False).json()
pprint(json.dumps(teams_get, indent=2, sort_keys=True))
teams = teams_get['items']
for team in teams:
    if team['name'] == 'Our Main Team':
        teamId = team['id']
        print(teamId)

rooms_body = {
    "title": "Our Main Room",
    "teamId": teamId
}
rooms_post = requests.post(rooms_url, headers=headers, data=json.dumps(rooms_body), verify=False).json()
rooms_get = requests.get(rooms_url, headers=headers, verify=False).json()
pprint(json.dumps(rooms_get, indent=2, sort_keys=True))
rooms = rooms_get['items']
for room in rooms:
    if room['title'] == 'Our Main Room':
        roomId = room['id']


msg_body = {
    "roomId": roomId,
    "text": "Python tutorials"
}
msg_post = requests.post(msg_url, headers=headers, data=json.dumps(msg_body), verify=False).json()
msg_get = requests.get(msg_url, headers=headers, verify=False).json()

