import yfinance as yf

class Api:

    def __init__(self):
        pass

    def request_history(self, symbol):
        ticker = yf.Ticker(str(symbol))
        return ticker.history(period="10y", interval="1d")