import requests
import json
import urllib3
from flask import Flask, request, make_response

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ngrok_url = 'https://d7a09831.ngrok.io'

app = Flask(__name__)
@app.route('/', methods=["POST", "GET"])
def index():
    content = request.get_json()
    print(content)
    if request.method == 'GET':
        try:
            validator = 'a20134ba4043b6a6436fe56dea8ba9c6f46fbeb4'
            response = make_response(validator)
            response.status_code = 200
            return response
        except Exception as ex:
            return 'Error'
            print(ex)

    elif request.method == 'POST':
        try:
            shared_secret = content['sharedSecret']
            if shared_secret == 'foo':
                content = request.get_json()
                print(content)
                return 'ok'
            else:
                response = make_response()
                response.status_code = 401
                return response + 'Unauthorized'

        except Exception as ex:
            response = make_response()
            response.status_code = 400
            return response + 'Bad request'
            print(ex)



if __name__ == '__main__':
    app.run(debug=True, port=8000)