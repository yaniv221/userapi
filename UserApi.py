import json

import requests

class UserApi:
    def __init__(self):
        self.url = "http://petstore.swagger.io/v2/"
        self.baseApi="user"

    def CreateUser(self,user):
        headers = {'content-type': 'application/json'}
        res = requests.post(self.url+ self.baseApi,data=json.dumps(user.GetUser()),headers=headers)
        res = requests.post(self.url + self.baseApi, json=user.GetUser())
        return res








    def GoogleCloud(self):
        URL = "https://maps.googleapis.com/maps/api/streetview"
        PARAMS = {'size': "1200x800",'location':"32.7927412,35.0376016","heading":"30","fov":"150"}
        r = requests.get(url=URL, params=PARAMS)
        with open("D:\image.png", 'wb') as f:
            f.write(r.content)
            f.close()
