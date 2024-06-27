import requests
import constants.defs as defs

class OandaApi:

    def __init__(self):
        self.session= requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {defs.API_KEY}",
            "Content-Type": "application/json"
        })