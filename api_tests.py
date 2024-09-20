from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
import time

from models.candle_timing import CandleTiming

if __name__ == '__main__':
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    # dd = api.last_complete_candle("EUR_USD", granularity="M5")
    # print(CandleTiming(dd))
    # api.place_trade("EUR_USD", 177, 1, take_profit=180, stop_loss=175)
    # trade_id = api.place_trade("EUR_USD", 23, 1)
    # print("opened: ", trade_id)
    # time.sleep(10)
    # print(f"Closing {trade_id}", api.close_trade(trade_id))   
    # [print(x) for x in api.get_open_trades()]
    print(api.get_prices(["GBP_JPY", "AUD_NZD"]))