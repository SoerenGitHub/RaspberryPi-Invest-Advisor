from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from scipy.signal import argrelextrema
import numpy as np
import pandas as pd

class Extrema:
    __arr = []

    def __init__(self, arr):
        self.__arr = pd.Series(arr)   

    def determine_max(self):
        extrema_max = argrelextrema(self.__arr.values, np.greater, order=5)[0]
        return self.__arr.iloc[extrema_max]

    def determine_min(self):
        extrema_min = argrelextrema(self.__arr.values, np.less, order=5)[0]
        return self.__arr.iloc[extrema_min]        

    def determine_global_max(self):
        extrema_max = np.argmax(self.__arr)
        return self.__arr.iloc[extrema_max]

    def determine_global_min(self):
        extrema_min = np.argmin(self.__arr)
        return self.__arr.iloc[extrema_min]