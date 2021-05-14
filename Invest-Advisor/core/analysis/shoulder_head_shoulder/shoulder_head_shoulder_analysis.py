from core.analysis.helper.simplifier import Simplifier
from core.analysis.helper.extrema import Extrema
import pandas as pd


class ShoulderHeadShoulderAnalysis:
    __simplify = None
    __trigger_zone = None
    __current_price = None
    __history = None
    
    def __init__(self, history, trigger_zone, trigger_peek, current_price) -> None:
        self.__simplify = Simplifier(history['Close'][-200:], trigger_peek, current_price).simplify()
        self.__trigger_zone = (current_price / 100) * trigger_zone
        self.__current_price = current_price

    def shs(self):

        return self.__simplify
        if(
            len(self.__simplify) == 7 and
            self.__inTriggerZone(self.__simplify.values[-1]) and
            self.__inTriggerZone(self.__simplify.values[-3]) &
            self.__inTriggerZone(self.__simplify.values[-5]) &
            self.__inTriggerZone(self.__simplify.values[-7]) &
            (
                (
                    self.__simplify.values[-2] < self.__simplify.values[-4] and
                    self.__simplify.values[-6] < self.__simplify.values[-4]
                ) |
                (
                    self.__simplify.values[-2] > self.__simplify.values[-4] and
                    self.__simplify.values[-6] > self.__simplify.values[-4]
                )
            )
        ):
            print('shs')
            return self.__simplify[-7:]
        else:
            return None
        

    def __inTriggerZone(self, price):
        return (
            (price < self.__current_price+self.__trigger_zone) &
            (price > self.__current_price-self.__trigger_zone)
        )