from pandas.core.series import Series
from pandas.core.frame import DataFrame
from process.models.iteratoritem import IteratorItem
from b_analysis.indicator import Indicator
from a_data.stock import Stock
import numpy as np

class Analysis:
    __indicators: list = None
    __stock: Stock = None
    __result: list[IteratorItem] = []

    def __init__(self, stock: Stock):
        self.__stock = stock

    def register(self, indicators: list):
        self.__indicators = indicators

    def analyse(self, iterator_item):
        self.__communicate_analyse(iterator_item)
        self.__result.append(iterator_item)
            #print([iterator_item])

    def __communicate_analyse(
        self,
        iterator_item_history: IteratorItem
    ):
        for indicator in self.__indicators:
            indicator.iterate_history(iterator_item_history)

    def get_result(self):
        return self.__result