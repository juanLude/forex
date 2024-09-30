from stream_bot.trade_settings_collection import tradeSettingsCollection

def run_bot():
    tradeSettingsCollection.load_trade_settings()
    tradeSettingsCollection.print_collection()