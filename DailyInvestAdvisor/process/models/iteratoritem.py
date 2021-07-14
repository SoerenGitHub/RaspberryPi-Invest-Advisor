from b_analysis.models.indicatorresult import IndicatorResult
from datetime import datetime

from pandas.core.series import Series
from pandas.core.frame import DataFrame

class IteratorItem(object):
    __index: int
    __length: int
    __date: datetime
    __high_price: float
    __low_price: float
    __open_price: float
    __close_price: float
    __volume: int
    __start: bool
    __end: bool
    __extrema: bool
    __all_lows: Series
    __all_highs: Series
    __all_closes: Series
    __all_opens: Series
    __all_volumes: Series
    __all_history: DataFrame
    __indicator_result: list[IndicatorResult]

    def __repr__(self): 
        return str(self.__date)+', \t'+str(self.__indicator_result)

    def __init__(
        self,
        index: int,
        length: int,
        date: datetime,
        high_price: float,
        low_price: float,
        open_price: float,
        close_price: float,
        volume: int,
        start: bool,
        end: bool,
        extrema: bool,
        all_lows: Series,
        all_highs: Series,
        all_closes: Series,
        all_opens: Series,
        all_volumes: Series,
        all_history: DataFrame,
        indicator_result: list
    ) -> None:
        self.__index = index
        self.__length = length
        self.__date = date
        self.__high_price = high_price
        self.__low_price = low_price
        self.__open_price = open_price
        self.__close_price = close_price
        self.__volume = volume
        self.__start = start
        self.__end = end
        self.__extrema = extrema
        self.__all_closes = all_closes
        self.__all_opens = all_opens
        self.__all_lows = all_lows
        self.__all_highs = all_highs
        self.__all_volumes = all_volumes
        self.__all_history = all_history
        self.__indicator_result = indicator_result

    def get_index(self):
        return self.__index

    def get_length(self):
        return self.__length

    def get_date(self):
        return self.__date

    def get_high_price(self):
        return self.__high_price

    def get_low_price(self):
        return self.__low_price

    def get_open_price(self):
        return self.__open_price

    def get_close_price(self):
        return self.__close_price

    def get_volume(self):
        return self.__volume

    def is_start(self):
        return self.__start

    def is_end(self):
        return self.__end

    def is_extrema(self):
        return self.__extrema

    def get_all_high_prices(self):
        return self.__all_highs

    def get_all_low_prices(self):
        return self.__all_lows

    def get_all_open_prices(self):
        return self.__all_opens

    def get_all_close_prices(self):
        return self.__all_closes

    def get_all_volumes(self):
        return self.__all_volumes

    def get_all_history(self):
        return self.__all_history

    def get_indicator_result(self):
        return self.__indicator_result



    
    def add_indicator_result(self, indicatorResult: IndicatorResult):
        self.__indicator_result.append(indicatorResult)
    
    @staticmethod
    def create_iterator_item(index, date, data, history):
        return IteratorItem(
                index,
                len(history),
                date,
                data['High'],
                data['Low'],
                data['Open'],
                data['Close'],
                data['Volume'],
                (index == 0),
                (index == len(history)-1),
                False,
                history['Low'],
                history['High'],
                history['Close'],
                history['Open'],
                history['Volume'],
                history,
                []
            )