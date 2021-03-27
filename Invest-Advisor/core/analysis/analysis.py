
from core.analysis.parabolic_sar.parabolic_sar import ParabolicSAR
from numpy import recfromtxt
from core.analysis.moving_average.moving_average_analysis import MovingAverage
from core.analysis.rsline.rsline_analysis import RSLineAnalysis
from core.analysis.helper.extrema import Extrema
from core.analysis.helper.simplifier import Simplifier


class Analysis:

    __rsline = None
    __ema = None
    __sma = None
    __psar = None

    def __init__(self, history) -> None:
        self.__history = history
       

    def analyse(self):
        extrema = Extrema(self.__history, 1)
        self.__rsline = RSLineAnalysis(extrema, 4, 8, 20, self.__history['Close'].values[-1]).rsline()

        moving_average = MovingAverage(self.__history, 5, 200, self.__history['Close'].values[-1])
        self.__ema = moving_average.ema()
        self.__sma = moving_average.sma()

        parabolic_sar = ParabolicSAR(self.__history, 5, 0.02, 0.2, self.__history['Close'].values[-1])
        self.__psar = parabolic_sar.psar()

    def has_analysis(self):
        has_analysis = (
            self.__rsline is not None or
            self.__ema is not None or
            self.__sma is not None or
            self.__psar is not None
        )
        return has_analysis

    def get_rsline(self):
        return self.__rsline

    def get_ema(self):
        return self.__ema

    def get_sma(self):
        return self.__sma

    def get_psar(self):
        return self.__psar