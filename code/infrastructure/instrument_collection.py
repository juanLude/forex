import json

from models.instrument import Instrument
class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = [ "name", "type", "displayName", "pipLocation","displayPrecision", "tradeUnitsPrecision", "marginRate" ]

    def __init__(self):
        self.instruments_dict = {}

    def LoadInstruments(self, path):
        self.instruments_dict = {}
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, 'r') as f:
            instruments_list = json.loads(f.read())
            for k,v in instruments_list.items():
                self.instruments_dict[k] = Instrument.FromApiObject(v)
    
    def PrintInstruments(self):
        [print(k,v) for k,v in self.instruments_dict.items()]
        print(len(self.instruments_dict.keys()), "instruments loaded.")