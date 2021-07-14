import pandas as pd
import numpy as np
from pandas._libs.tslibs import Timestamp
from scipy.signal import argrelextrema
import time
from datetime import datetime

class TrendTunnelAnalysis:

    def __init__(self, history, time_length) -> None:
        self.__history = pd.Series(history['Close']).sort_index(ascending=False)[:time_length]
        self.__time_length = time_length

    def timestamp_to_int(self, timestamp):
        return int(time.mktime(pd.Timestamp(timestamp).utctimetuple()))

    def trendtunnel(self):
        TT = pd.Series() 

        extrema_min_list = pd.Series(self.__history.iloc[argrelextrema(self.__history.values, np.less, order=1)[0]])
        extrema_max_list = pd.Series(self.__history.iloc[argrelextrema(self.__history.values, np.greater, order=1)[0]])

        n_index_max = len(extrema_max_list)
        for date, price in extrema_max_list.items():
            if(date == extrema_max_list.idxmax()):
                break
            n_index_max -= 1

        n_index_min = len(extrema_max_list)
        for date, price in extrema_max_list.items():
            if(date == extrema_max_list.idxmin()):
                break
            n_index_min -= 1

        pitch = (extrema_max_list.iloc[extrema_max_list.argmax()]-extrema_max_list.iloc[extrema_max_list.argmin()])/(n_index_max-n_index_min)
        print((extrema_max_list.iloc[extrema_max_list.argmax()]-extrema_max_list.iloc[extrema_max_list.argmin()]), (n_index_max-n_index_min))

        index = len(extrema_max_list)
        start_price = None
        end_price = None
        for date, price in extrema_max_list.items():
            if(index == len(extrema_max_list)):
                start_price = price

            value = start_price+(pitch*index)

            if(value < price):
                pitch = (extrema_max_list.iloc[extrema_max_list.argmax()]-price)/(n_index_max-index)
                start_price = -(index*pitch)+price
                end_price = start_price+(len(extrema_max_list)*pitch)

            
            index-=1
        
        print(pitch)
        TT = TT.append(pd.Series([start_price], index=[extrema_max_list.index[0]]))
        TT = TT.append(pd.Series([end_price], index=[extrema_max_list.index[-1]]))
        return TT
        

            


