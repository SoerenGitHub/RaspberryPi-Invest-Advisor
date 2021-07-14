from pandas.core.series import Series
import yfinance as yf

class Stock:
    __name: str = None
    __symbol: str = None
    __price: float = None
    __history: Series = None

    def __init__(self, name: str, symbol: str):
        self.__name = name
        self.__symbol = symbol

    def request_history(self):
        ticker = yf.Ticker(str(self.__symbol))
        self.__history = ticker.history(period="10y", interval="1d")

    #region Getter/Setter

    def get_history(self):
        return self.__history

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    #endregion Getter/Setter