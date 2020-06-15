import sys
import requests
import json 
import urllib3
from flask import Flask, request

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ngrok_URL = 'http://66da9436.ngrok.io'

webex_token = 'Bearer ZWRlZGU3N2QtNDhkYy00OTE0LTk4ZTgtNjMyYzdmZDc5MTVjMzQ3YzRkYzgtZDcw_PF84_bdc9a8b4-40e0-44a7-96eb-5e6cea4788dd'
path = '/rooms'
url = f'https://api.ciscospark.com/v1{path}'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': webex_token
}


def room():
    response = requests.get(url, headers=headers, verify=False).json()
    roomId = response['items'][0]['id']
    return roomId
    # print(json.dumps(response, indent=2, sort_keys=True))
    print(roomId)

room_Id = room()

def webhook_register():
    path = '/webhooks'
    url = f'https://api.ciscospark.com/v1{path}'
    payload = {
        "resource" : "messages",
        "event" : "created",
        "filter" : f"roomId={room_Id}",
        "targetUrl" : f"{ngrok_URL}",
        "name" : "WebEx Team Learning Lab Webhook"
    }          
    post_webhook = requests.post(url, headers=headers, verify=False,
        data=json.dumps(payload)).json()
    print(json.dumps(post_webhook, indent=2, sort_keys=True))

webhook_register()


def actual_message_parse(messageId):
    message_id = messageId
    path = f'/messages/{message_id}'
    url = f'https://api.ciscospark.com/v1{path}'
    response = requests.get(url, headers=headers, verify=False).json()
    message = response['text']
    return message



def weather_api(location):
    try:
        weather_api_key = 'ea8158d623a1487391695737200704'
        url = f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={location}'
        headers = {
          "Content-Type": "application/json",
          "Accept": "application/json",
        }
        response = requests.get(url, headers=headers, verify=False).json()
        # print(json.dumps(response, indent=2, sort_keys=True))
        temprature = response['current']['temp_c']
        feels_like = response['current']['feelslike_c']
        output = f"Bot: Temperature in {location} is {temprature}°, and it feels like {feels_like}°"
        return output
    except Exception as e:
        print(e)



def post_message(weather):
    try:
        url = "https://api.ciscospark.com/v1/messages"
        payload = {
            "roomId": room_Id,
            "text": weather
        }
        msg_post = requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()
    except Exception as e:
        print(e)



app = Flask(__name__)
@app.route('/', methods=["POST"])
def index():
    content = request.get_json()
    message_id = content['data']['id']
    location = actual_message_parse(message_id)
    location_parsed = location[0:16:1]

    if location_parsed == 'Bot: Temperature':
        sys.exit()
        return content
    else:
        weather = weather_api(location)
        post_message(weather)
        return content
        # print("Message has been created in the team")
        print (request.is_json)
        # return 'JSON posted'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
