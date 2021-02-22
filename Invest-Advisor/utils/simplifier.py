from numpy import index_exp
import pandas as pd
class Simplifier:
    __registered_peeks = pd.Series([])
    __grow_trend = None

    def __init__(self, to_simplify, trigger_zone, current_price) -> None:
        self.__trigger_zone = (current_price / 100) * trigger_zone
        self.__to_simplify = pd.Series(to_simplify)         
            
    def simplify(self):
        self.__registered_peeks = self.__registered_peeks.append(pd.Series([self.__to_simplify.iloc[0]], index=[self.__to_simplify.first_valid_index()]))
        for date, price in self.__to_simplify.items():
            if(pd.Series(self.__registered_peeks).iloc[-1]+self.__trigger_zone <= price):
                self.__grow_trend = True
                self.__registered_peeks = self.__registered_peeks.append(pd.Series([price], index=[date]))
            if(pd.Series(self.__registered_peeks).iloc[-1]-self.__trigger_zone >= price):
                self.__grow_trend = False
                self.__registered_peeks = self.__registered_peeks.append(pd.Series([price], index=[date]))
            if(
                ((self.__grow_trend == True) & (price > pd.Series(self.__registered_peeks).iloc[-1])) |
                ((self.__grow_trend == False) & (price < pd.Series(self.__registered_peeks).iloc[-1]))
            ):
                self.__registered_peeks = self.__registered_peeks.drop(index=self.__registered_peeks.last_valid_index())
                self.__registered_peeks = self.__registered_peeks.append(pd.Series([price], index=[date]))
        self.__registered_peeks = self.__registered_peeks.append(pd.Series([self.__to_simplify.iloc[-1]], index=[self.__to_simplify.last_valid_index()]))
        return self.__registered_peeks
        
