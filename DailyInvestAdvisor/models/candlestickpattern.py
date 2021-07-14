class CandlestickPattern:
    #region Variables
    __name: str = None
    __bull: bool = None
    __pattern: list = None
    __weight: float = None
    #endregion Variables

    def __init__(
        self, 
        name: str, 
        bull: bool, 
        pattern: list, 
        weight: float
    ) -> None:
        self.__name = name
        self.__bull = bull
        self.__pattern = pattern,
        self.__weight = weight

    #region Getter/Setter
    def getName(self):
        return self.__name

    def getPattern(self):
        return self.__pattern[0]

    def isBull(self):
        return self.__bull

    def getWeight(self):
        return self.__weight
    #endregion Getter/Setter