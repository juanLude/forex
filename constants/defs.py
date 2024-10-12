API_KEY= "7203735f4489a07b1fdaa82e0825b643-037a13c8ecd863561ee2fb38166bda77"
ACCOUNT_ID = "101-011-28651499-001"
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

SECURE_HEADER = {      
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

BUY = 1
SELL = -1
NONE = 0

MONGO_CONN_STR = "mongodb+srv://jmludevid:Ruggieri2733@cluster0.upqw8no.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"