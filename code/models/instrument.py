class Instrument:
    # Represents a financial instrument 
    
    def __init__(self, name, ins_type, display_name, pip_location, trade_units_precision, margin_rate):
        # 
        self.name = name
        self.ins_type = ins_type
        self.display_name = display_name
        self.pip_location = pow(10,pip_location)
        self.trade_units_precision = trade_units_precision
        self.margin_rate = float(margin_rate)

    def __repr__(self): # string representation to print the object
        return f"Instrument(name={self.name}, type={self.ins_type}, display_name={self.display_name}, pip_location={self.pip_location}, margin_rate={self.margin_rate})"
    
    @classmethod # decorator to define a class method that takes a dictionary and returns an Instrument object
    def FromApiObject(cls, api_object):
        return Instrument(
            name=api_object['name'],
            ins_type=api_object['type'],
            display_name=api_object['displayName'],
            pip_location=api_object['pipLocation'],
            trade_units_precision=api_object['tradeUnitsPrecision'],
            margin_rate=api_object['marginRate']
        )