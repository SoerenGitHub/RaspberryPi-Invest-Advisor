import pandas as pd
import numpy as np

class PastIndex:

    def __init__(self, history, trigger_zone, past_duration, current_price) -> None:
        self.__history = pd.Series(history)
        self.__past_duration = past_duration
        self.__trigger_zone = (current_price / 100) * trigger_zone
        self.__current_price = current_price

    def moving_average(self):
        SMA=pd.Series()
        for i in range(self.__past_duration,len(self.__history)):
            index = self.__history.index[i]
            SMA = SMA.append(pd.Series([self.__history[i-self.__past_duration:i].sum()/self.__past_duration], index=[index]))
        SMA[0:self.__past_duration]=SMA[self.__past_duration+1]
        return SMA

    def expotential_moving_average(self):
        SF=2./(self.__past_duration+1)
            
        EMA=pd.Series()
        EMA = EMA.append(self.__history.first(offset='3D'))
        for i in range(1,len(self.__history)):
            index = self.__history.index[i]
            EMA = EMA.append(pd.Series([EMA[i-1]+SF*(self.__history[i]-EMA[i-1])], index=[index]))
        return EMA

    def get_price(self):
        return self.__past_index_price
