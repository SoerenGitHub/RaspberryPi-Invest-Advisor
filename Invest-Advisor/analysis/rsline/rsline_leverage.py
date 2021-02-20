from analysis.rsline.rsline_analysis import RSLineAnalysis


class RSLineLeverage:

    __meaningfulness = False
    __buy = False
    __sell = False

    def __init__(self, rsline_analysis: RSLineAnalysis) -> None:
        self.__analysis = rsline_analysis
        if(self.__determine_meaningfulness()):
            self.__determine_decision()


    def __determine_meaningfulness(self) -> bool:
        return (
            (self.__analysis.get_price() != 0) &
            
        )
    
    def __determine_decision(self):
        if(self.__analysis.is_resistance()):
            self.__sell = True
        else:
            self.__buy = True

    def should_buy(self):
        return self.__buy

    def should_sell(self):
        return self.__sell