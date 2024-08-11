from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
import time

if __name__ == '__main__':
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    # api.place_trade("EUR_USD", 177, 1, take_profit=180, stop_loss=175)
    trade_id = api.place_trade("EUR_USD", 1901, 1)
    print("opened: ", trade_id)
    time.sleep(10)
    print(f"Closing {trade_id}", api.close_trade(trade_id))