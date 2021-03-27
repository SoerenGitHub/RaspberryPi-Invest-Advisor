from core.analysis.helper.simplifier import Simplifier
from core.analysis.analysis import Analysis
from data import Api
from utils import Graph
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
        graph = Graph(self.__history['Close'], 200)
        analysis = Analysis(self.__history)
        
        analysis.analyse()
        if analysis.has_analysis():
            if analysis.get_rsline() is not None:
                graph.draw_hline(analysis.get_rsline(), 'resistance/support')
            if analysis.get_ema() is not None:
                graph.draw_line(analysis.get_ema(), 'EMA')
            if analysis.get_sma() is not None:
                graph.draw_line(analysis.get_sma(), 'SMA')
            if(analysis.get_psar() is not None):
                graph.draw_line(analysis.get_psar()['bull'], 'PSAR(bull)', 'dotted')
                graph.draw_line(analysis.get_psar()['bear'], 'PSAR(bear)', 'dotted')

            today = date.today()
            graph_img = graph.save(self.__symbol, str(today))
            mail.addImage(graph_img, self.__symbol)
            return StockComponent(self.__name, self.__symbol, 'cid:{symbol}'.format(symbol=self.__symbol))
        else:
            return None
