class Instrument:
    
    def __init__(self,name, inst_type,displayName, pipLocation, tradeUnitsPrecision, marginRate):
        self.name = name
        self.inst_type = inst_type
        self.displayName = displayName
        self.pipLocation = pow(10, pipLocation)
        self.tradeUnitsPrecision = tradeUnitsPrecision
        self.marginRate = float(marginRate)

    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def FromApiObject(cls, ob):
        return Instrument(
            ob['name'],
            ob['ins_type'],
            ob['displayName'],
            ob['pipLocation'],
            ob['tradeUnitsPrecision'],
            ob['marginRate']    
        )