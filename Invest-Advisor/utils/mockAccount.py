class MockAccount:
    __money = 0; 

    def __init__(self):
        print('Mock Account is set!\n')

    def add(self, money):
        print('+'+str(money)+'€\n')
        self.__money += money

    def remove(self, money):
        print('-'+str(money)+'€\n')
        self.__money -= money