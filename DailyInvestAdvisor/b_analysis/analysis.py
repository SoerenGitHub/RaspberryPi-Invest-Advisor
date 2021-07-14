from pandas.core.series import Series
from pandas.core.frame import DataFrame
from models.iteratoritem import IteratorItem
from b_analysis.indicator import Indicator
from a_data.stock import Stock
import numpy as np

class Analysis:
    __indicators: list[Indicator] = None

    def register(self, indicators: list):
        self.__indicators = indicators

    def analyse(self, iterator_item: IteratorItem):
        for indicator in self.__indicators:
            iterator_item.add_indicator_result(indicator.iterate_analyse(iterator_item))