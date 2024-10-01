import copy
from queue import Queue
import threading

import pytz
from stream_example.stream_base import StreamBase
import datetime as dt

GRANULARITIES = {
    "M1": 1,
    "M5": 5,
    "M15": 15,
    "M30": 30,
    "H1": 60
}

class PriceProcessor(StreamBase):

    def __init__(self, shared_prices, price_lock: threading.Lock, price_events, logname, 
                 pair, granularity):
        super().__init__(shared_prices, price_lock, price_events, logname)
        self.pair = pair
        self.granularity = GRANULARITIES[granularity]

    def round_time_down(self, round_me: dt.datetime) -> dt.datetime:
        remainder = round_me.minute % self.granularity
        candle_time = dt.datetime(round_me.year, round_me.month, round_me.day, round_me.hour, 
                                  round_me.minute - remainder, tzinfo=pytz.timezone("UTC"))
        return candle_time
      


    def process_price(self):

        try:
            self.price_lock.acquire()
            price = copy.deepcopy(self.shared_prices[self.pair])
            #print("PriceProcessor: ", price)
        except Exception as error:
            self.log_message(f"CRASH : {error}", error=True)
        finally:
            self.price_lock.release()


    def run(self):

        while True:
            self.price_events[self.pair].wait()
            self.process_price()
            self.price_events[self.pair].clear()