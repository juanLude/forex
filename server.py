from flask import Flask, jsonify
from flask_cors import CORS

from api.oanda_api import OandaApi
from scraping.bloomberg_com import bloomberg_com
from scraping.investing_com import get_pair

app = Flask(__name__)
CORS(app)

@app.route("/api/test")
def test():
    return jsonify({"message": "Hello!"})

@app.route("/api/headlines")
def headlines():
    return jsonify(bloomberg_com())

@app.route("/api/technicals/<pair>/<tf>")
def technicals(pair, tf):
    data = get_pair(pair, tf)
    if data is None:
        return jsonify({"error": "pair not found"})
    return jsonify(data)

@app.route("/api/prices/<pair>/<granularity>/<count>")
def prices(pair, granularity, count):
    data = OandaApi().web_api_candles(pair, granularity, count)
    if data is None:
        return jsonify({"error": "error getting data"})
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)