import json

from models.instrument import Instrument
class InstrumentCollection:
    FILENAME = "instruments.json"
    API_KEYS = [ "name", "type", "displayName", "pipLocation","displayPrecision", "tradeUnitsPrecision", "marginRate" ]

    def __init__(self):
        self.instruments_dict = {}

    def LoadInstruments(self, path):
        self.instruments_dict = {} # reset dictionary
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, 'r') as f:
            instruments_list = json.loads(f.read())
            for k,v in instruments_list.items():
                self.instruments_dict[k] = Instrument.FromApiObject(v)
    def CreateFileFromApiData(self,api_data,path):
        if api_data == None:
            print("No API data provided.")
            return
  
        instruments_dict = {}
        for instrument_data in api_data:
            key = instrument_data['name']
            instruments_dict[key] = {k: instrument_data[k] for k in self.API_KEYS}
            
        fileName = f"{path}/{self.FILENAME}"
        with open(fileName, 'w') as f:
            f.write(json.dumps(instruments_dict, indent=4))

    def PrintInstruments(self):
        for k, v in self.instruments_dict.items():
            print(k, v)
        print(len(self.instruments_dict), "instruments loaded.")

instrumentCollection = InstrumentCollection()