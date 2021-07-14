from models.iteratoritem import IteratorItem
from pandas.core.frame import DataFrame
from b_analysis.analysis import Analysis
from pandas.core.series import Series
from ..indicator import Indicator

class PSAR(Indicator):
    _name: str = 'PSAR'

    __af: float = None
    __max_af: float = None
    __trigger_zone: float = None

    __psar = None
    __psarbull = None
    __psarbear = None
    __bull = True
    __af = None
    __ep = None
    __hp = None
    __lp = None
    __dates = None
    __current_price = None

    def __init__(self, trigger_zone: float, af: float, max_af: float) -> None:
        self.__trigger_zone = trigger_zone
        self.__af = af
        self.__max_af = max_af
        super().__init__()

    def init_analyse(self, iterator_item: IteratorItem):
                self.__psarbull = [None] * iterator_item.get_length()
                self.__psarbear = [None] * iterator_item.get_length()
                self.__ep = iterator_item.get_low_price()
                self.__hp = iterator_item.get_high_price()
                self.__lp = iterator_item.get_low_price()
                self.__dates = []
                self.__current_price = iterator_item.get_close_price()
                self.__psar = iterator_item.get_all_close_prices()[0:len(iterator_item.get_all_close_prices())]

    def determine_result(self):
        if(
            (self.__psar[-1] <= self.__current_price+self.__trigger_zone) &
            (self.__psar[-1] >= self.__current_price-self.__trigger_zone)
        ):
            return DataFrame({'bull': self.__psarbull, 'bear': self.__psarbear}, index=self.__dates)
        else:
            return None

    def iterate_history(self, iterator_item: IteratorItem):
        if(iterator_item.is_start()):
            self.init_analyse(iterator_item)

        self.__dates.append(iterator_item.get_date())
        if(iterator_item.get_index() >= 2):            
            if self.__bull:
                self.__psar[iterator_item.get_index()] = self.__psar[iterator_item.get_index() - 1] + self.__af * (self.__hp - self.__psar[iterator_item.get_index() - 1])
            else:
                self.__psar[iterator_item.get_index()] = self.__psar[iterator_item.get_index() - 1] + self.__af * (self.__lp - self.__psar[iterator_item.get_index() - 1])
            reverse = False
            if self.__bull:
                if iterator_item.get_low_price() < self.__psar[iterator_item.get_index()]:
                    self.__bull = False
                    reverse = True
                    self.__psar[iterator_item.get_index()] = self.__hp
                    self.__lp = iterator_item.get_low_price()
                    self.__af = self.__af
            else:
                if iterator_item.get_high_price() > self.__psar[iterator_item.get_index()]:
                    self.__bull = True
                    reverse = True
                    self.__psar[iterator_item.get_index()] = self.__lp
                    self.__hp = iterator_item.get_high_price()
                    self.__af = self.__af
            if not reverse:
                if self.__bull:
                    if iterator_item.get_high_price() > self.__hp:
                        self.__hp = iterator_item.get_high_price()
                        self.__af = min(self.__af + self.__af, self.__max_af)
                    if iterator_item.get_all_low_prices()[iterator_item.get_index() - 1] < self.__psar[iterator_item.get_index()]:
                        self.__psar[iterator_item.get_index()] = iterator_item.get_all_low_prices()[iterator_item.get_index() - 1]
                    if iterator_item.get_all_low_prices()[iterator_item.get_index() - 2] < self.__psar[iterator_item.get_index()]:
                        self.__psar[iterator_item.get_index()] = iterator_item.get_all_low_prices()[iterator_item.get_index() - 2]
                else:
                    if iterator_item.get_low_price() < self.__lp:
                        self.__lp = iterator_item.get_low_price()
                        self.__af = min(self.__af + self.__af, self.__max_af)
                    if iterator_item.get_all_high_prices()[iterator_item.get_index() - 1] > self.__psar[iterator_item.get_index()]:
                        self.__psar[iterator_item.get_index()] = iterator_item.get_all_high_prices()[iterator_item.get_index() - 1]
                    if iterator_item.get_all_high_prices()[iterator_item.get_index() - 2] > self.__psar[iterator_item.get_index()]:
                        self.__psar[iterator_item.get_index()] = iterator_item.get_all_high_prices()[iterator_item.get_index() - 2]
            if self.__bull:
                self.__psarbull[iterator_item.get_index()] = self.__psar[iterator_item.get_index()]
            else:
                self.__psarbear[iterator_item.get_index()] = self.__psar[iterator_item.get_index()]


        if(iterator_item.is_end()):
            self.__result = self.determine_result()
        
