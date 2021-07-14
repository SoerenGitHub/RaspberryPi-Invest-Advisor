class StockComponent:

    def __init__(self, name, symbol, graph) -> None:
        self.__name = name
        self.__symbol = symbol
        self.__graph = graph
    
    def get_html(self):
        component = open('./presentation/templates/stock/stock_component.html', 'r').read()
        return component.format(
                name=self.__name,
                symbol=self.__symbol,
                graph=self.__graph
            )

    @staticmethod
    def get_css():
        return open('./presentation/templates/stock/stock_component.css', 'r').read()