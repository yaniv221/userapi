import json

import requests


def GoogleCloud():
        URL = "https://maps.googleapis.com/maps/api/streetview"
        PARAMS = {'size': "1200x800", 'location': "32.8136631,35.1268774", "heading": "270", "fov": "300"}
        r = requests.get(url=URL, params=PARAMS)
        with open("D:\image3.png", 'wb') as f:
            f.write(r.content)
            f.close()



GoogleCloud()
