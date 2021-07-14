from typing import Any


class IndicatorResult(object):
    __indicatorName: str = None
    __weight: float = None
    __value: Any = None
    __bull: bool = None

    def __init__(self, name, weight, value, bull) -> None:
        self.__indicatorName = name
        self.__weight = weight
        self.__value = value
        self.__bull = bull
        super().__init__()

    def __repr__(self): 
        return self.__indicatorName+', \t'+str(self.__weight)+', \t'+ str(self.__value)+', \t'+str(self.__bull)

    #region Getter/Setter
    def getIndicatorName(self):
        return self.__indicatorName

    def getWeight(self):
        return self.__weight

    def getValue(self):
        return self.__value
    
    def isBull(self):
        return self.__bull
    #endregion Getter/Setter