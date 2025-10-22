from api.oanda_api import OandaAPI

if __name__ == "__main__":
    api = OandaAPI()
    # You can now use oanda_api to access OANDA API endpoints
    print("OANDA API client initialized.")
    data = api.get_account_instruments()
    print("Instruments:", data)