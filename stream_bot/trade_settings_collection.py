

import json


class TradeSettingsCollection:

    FILENAME = "settings.json"

    def __init__(self):
        self.trade_settings_dict = {}
        self.granularity = "H1"
        self.trade_risk = 1.0

    def load_trade_settings(self):
        self.trade_settings_dict = {}  
        fileName = f"./stream_bot/{self.FILENAME}"
        with open(fileName, "r") as f:
            data = json.loads(f.read())
            self.granularity = data['granularity']
            self.trade_risk = data['trade_risk']