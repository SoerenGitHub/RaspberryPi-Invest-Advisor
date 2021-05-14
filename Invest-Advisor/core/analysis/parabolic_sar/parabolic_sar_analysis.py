from numpy import column_stack
import pandas as pd


class ParabolicSarAnalysis:

    def __init__(self, history, trigger_zone, af, max_af, current_price) -> None:
        self.__history = history
        self.__trigger_zone = (current_price / 100) * trigger_zone
        self.__current_price = current_price
        self.__af = af
        self.__max_af = max_af

    def psar(self, iaf = None, maxaf = None):
        if (iaf is None):
            iaf = self.__af
        if (maxaf is None):
            maxaf = self.__max_af
        length = len(self.__history)
        dates = list(pd.DataFrame(self.__history).index)
        high = list(self.__history['High'])
        low = list(self.__history['Low'])
        close = list(self.__history['Close'])
        psar = close[0:len(close)]
        psarbull = [None] * length
        psarbear = [None] * length
        bull = True
        af = iaf
        ep = low[0]
        hp = high[0]
        lp = low[0]
        for i in range(2,length):
            if bull:
                psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
            else:
                psar[i] = psar[i - 1] + af * (lp - psar[i - 1])
            reverse = False
            if bull:
                if low[i] < psar[i]:
                    bull = False
                    reverse = True
                    psar[i] = hp
                    lp = low[i]
                    af = iaf
            else:
                if high[i] > psar[i]:
                    bull = True
                    reverse = True
                    psar[i] = lp
                    hp = high[i]
                    af = iaf
            if not reverse:
                if bull:
                    if high[i] > hp:
                        hp = high[i]
                        af = min(af + iaf, maxaf)
                    if low[i - 1] < psar[i]:
                        psar[i] = low[i - 1]
                    if low[i - 2] < psar[i]:
                        psar[i] = low[i - 2]
                else:
                    if low[i] < lp:
                        lp = low[i]
                        af = min(af + iaf, maxaf)
                    if high[i - 1] > psar[i]:
                        psar[i] = high[i - 1]
                    if high[i - 2] > psar[i]:
                        psar[i] = high[i - 2]
            if bull:
                psarbull[i] = psar[i]
            else:
                psarbear[i] = psar[i]
        if(
            (psar[-1] <= self.__current_price+self.__trigger_zone) &
            (psar[-1] >= self.__current_price-self.__trigger_zone)
        ):
            return pd.DataFrame({'bull': psarbull, 'bear': psarbear}, index=dates)
        else:
            return None
        