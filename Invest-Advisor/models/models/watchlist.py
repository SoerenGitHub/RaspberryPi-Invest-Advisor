class Watchlist:
    __stocks = []

    def add_stock(self, stock):
        print(str(stock.get_name()) + ' is added to the watchlist\n')
        self.__stocks.append(stock)

    def remove_stock(self, stock):
        print(str(stock.get_name()) + ' is removed to the watchlist\n')
        self.__stocks.remove(stock)