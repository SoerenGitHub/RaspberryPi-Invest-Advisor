from core.analysis.helper.simplifier import Simplifier
from core import Analysis
from data import Api
from utils import Graph
from presentation import StockComponent
from datetime import date
import pandas as pd


class Stock:
    __name = 'default'
    __score = 0
    __currentValue = 0
    __buyValue = 0
    __history = []
    __graph_image = None
    __analysis = None

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

    def get_graph_image(self):
        return self.__graph_image

    def get_analysis(self):
        return self.__analysis

    def buy(self):
        print('buy ' + self.name + ' for ' + self.__currentValue)
        self.__buyValue = self.__currentValue
    
    def sell(self):
        print('sell ' + self.name + ' for ' + self.__currentValue)
        self.__buyValue = 0

    def add_score(self, score):
        self.__score += score

    def create_component(self):
        graph = Graph(self.__history['Close'], 200)
        self.__analysis = Analysis(self.__history)
        self.__analysis.analyse()
        if self.__analysis.has_analysis():
            if self.__analysis.get_rsline() is not None:
                graph.draw_hline(self.__analysis.get_rsline(), 'resistance/support')
            if self.__analysis.get_ema() is not None:
                graph.draw_line(self.__analysis.get_ema(), 'EMA')
            if self.__analysis.get_sma() is not None:
                graph.draw_line(self.__analysis.get_sma(), 'SMA')
            if(self.__analysis.get_psar() is not None):
                graph.draw_line(self.__analysis.get_psar()['bull'], 'PSAR(bull)', 'dotted')
                graph.draw_line(self.__analysis.get_psar()['bear'], 'PSAR(bear)', 'dotted')
            #if(self.__analysis.get_shs() is not None):
             #   graph.draw_line(self.__analysis.get_shs(), 'SHS')

            today = date.today()
            self.__graph_image = graph.save(self.__symbol, str(today))
            return StockComponent(self.__name, self.__symbol, 'cid:{symbol}'.format(symbol=self.__symbol))
        else:
            return None
