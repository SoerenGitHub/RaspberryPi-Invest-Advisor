from pandas.tseries.frequencies import to_offset
from utils.graph import Graph
from analysis.rsline.rsline_analysis import RSLineAnalysis
from analysis.extrema.extrema import Extrema
from analysis.rsline.rsline_leverage import RSLineLeverage


import pandas as pd

class RSLineSimulation:

    def __init__(self, stock_history, past_view, deviation, trigger_zone, trigger_peek, extrema_order) -> None:
        self.__stock_history = stock_history
        self.__deviation = deviation
        self.__trigger_zone = trigger_zone
        self.__trigger_peek = trigger_peek
        self.__extrema_order = extrema_order
        self.__past_view = past_view
        self.__simulate()

    def __simulate(self):
        for x in range(self.__past_view, len(self.__stock_history)):
            view = pd.Series(pd.Series(self.__stock_history).sort_index(ascending=True))[x-self.__past_view:x]
            extrema = Extrema(view, self.__extrema_order)
            rsline = RSLineAnalysis(extrema, self.__deviation, self.__trigger_zone, self.__trigger_peek, view.values[-1])
            rsline_leverage = RSLineLeverage(rsline)
            if(rsline_leverage.should_buy()):
                print(' buy -> ' + str(view.last_valid_index()))
                graph = Graph(self.__stock_history, 'simulation')
                graph.draw_up_arrow(view.last('2D'))
                graph.draw_hline(rsline.get_price())
                graph.show()
            if(rsline_leverage.should_sell()):
                print('sell -> '+ str(view.last_valid_index()))
                graph = Graph(self.__stock_history, 'simulation')
                graph.draw_down_arrow(view.last('2D'))
                graph.draw_hline(rsline.get_price())
                graph.show()