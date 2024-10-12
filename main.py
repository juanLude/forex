
from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ema_macd_mp import run_ema_macd
from simulation.ma_cross import run_ma_sim
from dateutil import parser
from infrastructure.collect_data import run_collection
from stream_example.streamer import run_streamer
from db.db import DataDB

if __name__ == '__main__':
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    #stream_prices(['GBP_JPY', 'AUD_NZD'])
    #run_ema_macd(instrumentCollection)
    # run_collection(instrumentCollection,api)
    #run_ma_sim()
    # print(api.fetch_candles("EUR_USD",granularity="D",price="MB"))
    # data = api.get_account_summary()
    # print(data)

    # instrumentCollection.CreateFile(api.get_account_instruments(),"./data")
    # instrumentCollection.LoadInstruments("./data")
    # instrumentCollection.PrintInstruments()
    # run_ma_sim(curr_list=["EUR","USD","GBP"]) 
    # run_ema_macd(instrumentCollection)
    # run_streamer()
    d = DataDB()
    d.test_connection()