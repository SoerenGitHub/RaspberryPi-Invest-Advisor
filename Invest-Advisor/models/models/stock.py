from data import Api
from utils import Graph
from core import RSLineAnalysis, Extrema
from presentation import StockComponent
from datetime import date


class Stock:
    __name = 'default'
    __score = 0
    __currentValue = 0
    __buyValue = 0
    __history = []

    def __init__(self, name, symbol):
        self.__name = name
        self.__history = Api().request_history(symbol)
        self.__symbol = symbol

    def set_currentValue(self, value):
        self.__currentValue = value

    def get_currentCalue(self):
        return self.__currentValue

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_history(self):
        return self.__history

    def buy(self):
        print('buy ' + self.name + ' for ' + self.__currentValue)
        self.__buyValue = self.__currentValue
    
    def sell(self):
        print('sell ' + self.name + ' for ' + self.__currentValue)
        self.__buyValue = 0

    def add_score(self, score):
        self.__score += score

    def create_component(self, mail):
        graph = Graph(self.__history['Close'], self.__symbol)
        extrema = Extrema(self.__history['Close'], 1)
        rsline = RSLineAnalysis(extrema, 4, 6, 20, self.__history['Close'].values[-1])
        if(rsline.get_price() != 0):
            graph.draw_hline(rsline.get_price())
        today = date.today()
        graph_img = graph.save(self.__symbol, str(today))
        mail.addImage(graph_img, self.__symbol)
        return StockComponent(self.__name, self.__symbol, 'cid:{symbol}'.format(symbol=self.__symbol))
