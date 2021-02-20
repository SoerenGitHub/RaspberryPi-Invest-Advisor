class Stock:
    __name = 'default'
    __score = 0
    __currentValue = 0
    __buyValue = 0
    __history = []

    def __init__(self, name, symbol, history):
        self.__name = name
        self.__history = history
        self.__symbol = symbol

    def set_currentValue(self, value):
        self.__currentValue = value

    def get_currentCalue(self):
        return self.__currentValue

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_history(self):
        return self.__history

    def buy(self):
        print('buy ' + self.name + ' for ' + self.__currentValue)
        self.__buyValue = self.__currentValue
    
    def sell(self):
        print('sell ' + self.name + ' for ' + self.__currentValue)
        self.__buyValue = 0

    def add_score(self, score):
        self.__score += score