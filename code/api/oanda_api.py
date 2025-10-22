# create a class that contains all the endpoints for the OANDA 

import requests
import os
from dotenv import load_dotenv
load_dotenv()

class OandaAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {os.getenv("OANDA_API_KEY")}',
            'Content-Type': 'application/json'
        })
    
    def make_request(self, url, verb='GET', code=200, params=None, data=None, headers=None):

        full_url = f'{os.getenv("OANDA_URL")}/{url}'
        try:
            response = None
            if verb == 'GET':
                response = self.session.get(full_url, params=params, headers=headers)   
            if response == None:
                return False, {'Unsupported HTTP verb'}
            if response.status_code == code:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as error:
            return False, {'Exception': error}
        
    
    def get_account_endpoint(self, endpoint, data_key):
        url = f'accounts/{os.getenv("OANDA_ACCOUNT_ID")}/{endpoint}'
        success, response = self.make_request(url)
        if success:
            return response[data_key]
        else:
            print("Error fetching account endpoint:", response)
            return None
    def get_account_summary(self):
        return self.get_account_endpoint('summary', 'account')
    
    def get_account_instruments(self):
        return self.get_account_endpoint('instruments', 'instruments')
        