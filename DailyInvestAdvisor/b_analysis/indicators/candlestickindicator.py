from pandas.core.frame import DataFrame
from pandas.core.generic import NDFrame
from ..indicator import Indicator
from models.iteratoritem import IteratorItem
from models.indicatorresult import IndicatorResult
from models.candlestickpattern import CandlestickPattern


class CandlestickIndicator(Indicator):
    _name: str = 'Candlestick'
    _weight: float = 0.5
    _weight_sensitiv = 0.01

    __patterns: list[CandlestickPattern] = [
        CandlestickPattern(
            'Hammer +', 
            True, 
            [
                (False),
                (False),
                (False),
                (False),
                ((0, 5), (0, 20), (75, 100))
            ],
            0.8
        ),

        CandlestickPattern(
            'Hanging Man -', 
            False, 
            [
                (True),
                (True),
                (True),
                (True),
                ((0, 5), (0, 20), (75, 100))
            ],
            0.8
        ),

        CandlestickPattern(
            'Inverted Hammer +', 
            True,
            [
                (False),
                (False),
                (False),
                ((0, 25), (100, 25), (0, 25), False),
                ((75, 100), (0, 20), (0, 5))
            ],
            0.6
        ),

        CandlestickPattern(
            'Shooting Star -', 
            False,
            [
                (True),
                (True),
                (True),
                ((0, 25), (100, 25), (0, 25), True),
                ((75, 100), (0, 20), (0, 5))
            ],
            0.6
        ),
        
        CandlestickPattern(
            'Belt Hold +', 
            True,
            [
                (False),
                (False),
                (False),
                (False),
                ((10,40), (60, 95), (0,5), True)
            ],
            0.9
        ),
        
        CandlestickPattern(
            'Belt Hold -', 
            False,
            [
                (True),
                (True),
                (True),
                (True),
                ((0,5), (60, 95), (10,40), False)
            ],
            0.9    
        ),

        CandlestickPattern(
            'Engulfing +', 
            True,
            [
                (False),
                (False),
                (False),
                ((5, 25), (30, 60), (5, 25), False),
                ((5, 18), (65, 80), (5, 18), True)
            ],
            0.95
        ),

        CandlestickPattern(
            'Engulfing -',
            False,
            [
                (True),
                (True),
                (True),
                 ((5, 25), (30, 60), (5, 25), True),
                ((5, 18), (65, 80), (5, 18), False)
            ],
            0.95
        )
        #HARAMI = CandlestickPattern('Harami +', True)
        #HARAMI_= CandlestickPattern('Harami -', False)
        #HARAMI_CROSS = CandlestickPattern('Harami Cross +', True)
        #HARAMI_CROSS_ = CandlestickPattern('Harami Cross -', False)
        #PIERCING_LINE = CandlestickPattern('Piercing Line +', True)
        #DARK_CLOUD_COVER_ = CandlestickPattern('Dark Cloud Cover -', False)
        #DOJI_STAR = CandlestickPattern('Doji Star +', True)
        #DOJI_STAR_ = CandlestickPattern('Doji Star -', False)
        #MEETING_LINE = CandlestickPattern('Meeting Line +', True)
        #MEETING_LINE_ = CandlestickPattern('Meeting Line -', False)
        #THREE_WHITE_SOLDIER = CandlestickPattern('Three White Soldier +', True)
        #THREE_BLACK_Crows_ = CandlestickPattern('Three_Black_Crows -', False)
        #MORNING_STAR = CandlestickPattern('Morning Star +', True)
        #EVENING_STAR_ = CandlestickPattern('Evening Star -', False)
        #MORNING_DOJI_STAR = CandlestickPattern('Morning Doji Star +', True)
        #EVENING_DOJI_STAR_ = CandlestickPattern('Evening_Doji Star -', False)
        #ABADONED_BABY = CandlestickPattern('Abadoned Baby +', True)
        #ABADONED_BABY_ = CandlestickPattern('Abadoned Baby -', False)
        #TRI_STAR = CandlestickPattern('Tri Star +', True)
        #TRI_STAR_ = CandlestickPattern('Tri Star -', True)
        #BREAKAWAY = CandlestickPattern('Beakaway +', True)
        #BREAKAWAY_ = CandlestickPattern('Breakaway -', False)
        #THREE_INSIDE_UP = CandlestickPattern('Three Inside Up +', True)
        #THREE_INSIDE_DOWN = CandlestickPattern('Three Inside Down -', False)
        #... BUCH ...
    ]

    def __init__(self) -> None:
        super().__init__()
        
    def iterate_analyse(self, iterator_item: IteratorItem) -> None:
         if(iterator_item.get_index() > 4):
            past5days = DataFrame(iterator_item.get_all_history()[iterator_item.get_index()-5:iterator_item.get_index()])
            return self.candlestickPattern(past5days)

    def inPercent(self, candlestick: DataFrame, from_value: str, to_value: str) -> float:
        if((candlestick['High'] - candlestick['Low']) == 0):
            return 0
        
        if((candlestick[from_value] - candlestick[to_value]) == 0):
            return 0

        return ((candlestick[from_value] - candlestick[to_value])/(candlestick['High'] - candlestick['Low']))*100

    def candlestickPattern(self, past5days: DataFrame) -> IndicatorResult:
        self.__patterns.sort(key=lambda x: x.getWeight(), reverse=True)
        for pattern in self.__patterns:
            for dayIndex, (date, candlestick) in enumerate(past5days.iterrows()):
                
                #calculate Candlestick zones
                bull: bool = (candlestick['Open'] < candlestick['Close'])
                top = None
                middle = None
                bottom = None
                if(bull):
                    top = self.inPercent(candlestick, 'High', 'Close')
                    middle = self.inPercent(candlestick, 'Close', 'Open')
                    bottom = self.inPercent(candlestick, 'Open', 'Low')
                else:
                    top = self.inPercent(candlestick, 'High', 'Open')
                    middle = self.inPercent(candlestick, 'Open', 'Close')
                    bottom = self.inPercent(candlestick, 'Close', 'Low')
                  
                #determine Candlestick Pattern
                if(
                    isinstance(pattern.getPattern()[dayIndex], bool) and
                    pattern.getPattern()[dayIndex] != bull
                ):
                    break

                if(
                    not isinstance(pattern.getPattern()[dayIndex], bool)
                ):
                    if(
                        top <= pattern.getPattern()[dayIndex][0][0]
                        or top >= pattern.getPattern()[dayIndex][0][1]
                    ):
                        break

                    if(
                        middle <= pattern.getPattern()[dayIndex][1][0]
                        or middle >= pattern.getPattern()[dayIndex][1][1]
                    ):
                        break

                    if(
                        bottom <= pattern.getPattern()[dayIndex][2][0]
                        or bottom >= pattern.getPattern()[dayIndex][2][1]
                    ):
                        break

                    if(
                        bull != None
                        and len(pattern.getPattern()[dayIndex]) == 4
                        and bull != pattern.getPattern()[dayIndex][3]
                    ):
                        break

                if(dayIndex == 4):
                    return IndicatorResult(self._name, pattern.getWeight(), pattern.getName(), pattern.isBull())
        return None
