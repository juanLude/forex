import requests
import constants.defs as defs
import dateutil as parser
from datetime import datetime as dt
class OandaApi:

    def __init__(self):
        self.session= requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {defs.API_KEY}",
            "Content-Type": "application/json"
        })

    def make_request(self, url, verb='get',code =200, params=None, data=None,headers=None):
        full_url = f"{defs.OANDA_URL}/{url}"
        try:
            response= None
            if verb == "get":
                response = self.session.get(full_url, params=params, data=data, headers=headers)
            if response == None:
                return False, {'error': 'verb not found'}
            if response.status_code == code:
                return True,response.json()
            else:
                return False,response.json()

        except Exception as error:
            return False,{'Exception': error}
    
    # get account endpoint
    def get_account_ep(self, ep, data_key):
        url = f"accounts/{defs.ACCOUNT_ID}/{ep}"
        ok, data = self.make_request(url)
        if ok == True and data_key in data:
            return data[data_key]
        else:
            print("Error get_account_ep",data)
            return None
        
    def get_account_summary(self):
        return self.get_account_ep("summary","account")
    
    def get_account_instruments(self):
        return self.get_account_ep("instruments","instruments")
    

    def fetch_candles(self, pair_name, count=10, granularity="H1", price="MBA", date_from=None, date_to=None):
        url = f"instruments/{pair_name}/candles"
        params = dict(
             
            granularity=granularity,
            price=price
            )

        if date_from != None and date_to != None:
            params['to'] = date_to
            params['from'] = date_from
            
        response =session.get(url,params=params, data=None,headers=None)
        data = response.json()

        if response.status_code == 200:
            if 'candles' not in data:
                data = []
            else:
                data = data['candles']
        return response.status_code, data

    def get_candles_df(data):
        if len(data) == 0:
            return pd.DataFrame()
            
        prices = ['mid','bid','ask']
        ohlc = ['o','h','l','c']   
        
        final_data = []
        for candle in data:
            if candle['complete']== False:
                continue
            new_dict = {}
            new_dict['time'] = parser.parse(candle['time'])
            new_dict['volume'] = candle['volume']
            for p in prices:
                for o in ohlc:
                    new_dict[f"{p}_{o}"]= float(candle[p][o])
            final_data.append(new_dict)
        df = pd.DataFrame.from_dict(final_data)
        return df