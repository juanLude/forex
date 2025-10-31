from api.oanda_api import OandaAPI
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_simulation
if __name__ == "__main__":
    api = OandaAPI()
    # You can now use oanda_api to access OANDA API endpoints
    # print("OANDA API client initialized.")
    # data = api.get_account_instruments()
    # print("Instruments:", data)
    # instrumentCollection.LoadInstruments("./exploration/")
    # instrumentCollection.PrintInstruments()
    #instrumentCollection.CreateFileFromApiData(api.get_account_instruments(),"./exploration")
    # instrumentCollection.LoadInstruments(".exploration/data")
    # instrumentCollection.PrintInstruments()
    run_ma_simulation(curr_list=["EUR","USD", "GBP"]) 