from models.indicatorresult import IndicatorResult
from pandas.core import series
from models.iteratoritem import IteratorItem

class Indicator(object):
    _name: str = None
    _weight: float = None
    _weight_sensitiv: float = None

    def __init__(self) -> None:
        pass

    def iterate_analyse(self, iterator_item: IteratorItem) -> IndicatorResult:
        pass

    def iterate_weight(self, iterator_item: IteratorItem) -> None: 
        if(self._weight_sensitiv > 0):
            for result in iterator_item.get_indicator_result():
                if( result and result.getIndicatorName() == self._name):
                    if(
                        iterator_item.get_all_close_prices()[iterator_item.get_index()+1] > iterator_item.get_close_price()
                        and (self._weight + (self._weight*self._weight_sensitiv)) < 1
                    ):
                        self._weight = self._weight + (self._weight*self._weight_sensitiv)
                    elif(
                        iterator_item.get_all_close_prices()[iterator_item.get_index()+1] < iterator_item.get_close_price()
                        and (self._weight - (self._weight*self._weight_sensitiv)) > 0
                    ):
                        self._weight = self._weight - (self._weight*self._weight_sensitiv)
                    
                    print(self._name + ' ' + str(self._weight))