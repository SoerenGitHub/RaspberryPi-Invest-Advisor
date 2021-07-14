from b_analysis.indicator import Indicator
from models.iteratoritem import IteratorItem

class Score:
    __indicators: list[Indicator] = None

    def register(self, indicators: list):
        self.__indicators = indicators

    def scoring(self, iterator_item: IteratorItem):
        for indicator in self.__indicators:
            indicator.iterate_weight(iterator_item)