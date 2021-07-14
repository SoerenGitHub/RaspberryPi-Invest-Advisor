
from core.analysis.parabolic_sar.parabolic_sar_analysis import ParabolicSarAnalysis
from core.analysis.shoulder_head_shoulder.shoulder_head_shoulder_analysis import ShoulderHeadShoulderAnalysis
from numpy import recfromtxt
from core.analysis.moving_average.moving_average_analysis import MovingAverageAnalysis
from core.analysis.rsline.rsline_analysis import RSLineAnalysis
from core.analysis.trendtunnel.trendTunnel_analysis import TrendTunnelAnalysis
from core.analysis.helper.extrema import Extrema


class Analysis:

    __rsline = None
    __ema = None
    __sma = None
    __psar = None
    __shs = None
    __tt = None

    def __init__(self, history) -> None:
        self.__history = history
       

    def analyse(self):
        extrema = Extrema(self.__history, 1)
        self.__rsline = RSLineAnalysis(extrema, 4, 8, 20, self.__history['Close'].values[-1]).rsline()

        moving_average = MovingAverageAnalysis(self.__history, 5, 200, self.__history['Close'].values[-1])
        self.__ema = moving_average.ema()
        self.__sma = moving_average.sma()

        parabolic_sar = ParabolicSarAnalysis(self.__history, 5, 0.02, 0.2, self.__history['Close'].values[-1])
        self.__psar = parabolic_sar.psar()

        trend_tunnel = TrendTunnelAnalysis(self.__history, 200)
        self.__tt = trend_tunnel.trendtunnel()

        #shoulder_head_shoulder = ShoulderHeadShoulderAnalysis(self.__history, 10, 15, self.__history['Close'].values[-1])
        #self.__shs = shoulder_head_shoulder.shs()

    def has_analysis(self):
        has_analysis = (
            self.__rsline is not None or
            self.__ema is not None or
            self.__sma is not None or
            self.__psar is not None or
            self.__shs is not None or
            self.__tt is not None
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

    def get_shs(self):
        return self.__shs

    def get_tt(self):
        return self.__tt