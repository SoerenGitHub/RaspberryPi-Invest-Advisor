from b_analysis.models.indicatorresult import IndicatorResult
from pandas.core import series
from process.models.iteratoritem import IteratorItem

class Indicator(object):
    _name: str = None

    def __init__(self) -> None:
        pass

    def iterate_history(self, iterator_item: IteratorItem) -> None:
        pass