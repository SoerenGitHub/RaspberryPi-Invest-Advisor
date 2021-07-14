from b_analysis.indicators.candlestickindicator import CandlestickIndicator
from c_scoring.score import Score
from models.iteratoritem import IteratorItem
from pandas.core.frame import DataFrame
from pandas.core.frame import Series
from b_analysis.indicators.psar import PSAR
from b_analysis.analysis import Analysis
import threading
from a_data.stock import Stock
from d_drawing.graph import Graph

class Process(threading.Thread):
    __stock: Stock = None
    __analysis: Analysis = None
    __score: Score = None

    def __init__(self, stock: Stock):
        threading.Thread.__init__(self)
        self.__stock = stock
        self.__analysis = Analysis()
        self.__score = Score()

    def run(self):
        self.__stock.request_history()

        self.__analysis.register([
            #PSAR(5, 0.02, 0.2),
            CandlestickIndicator()
        ])

        self.__score.register([
            #PSAR(5, 0.02, 0.2),
            CandlestickIndicator()
        ])

        history: Series = self.__stock.get_history()
        index: int = -1

        for date, data in DataFrame(history).sort_index(ascending=True).iterrows():
            index += 1
            iterator_item = IteratorItem.create_iterator_item(index, date, data, history)

            self.__analysis.analyse(iterator_item)
            self.__score.scoring(iterator_item)
        


        

        #Present Result