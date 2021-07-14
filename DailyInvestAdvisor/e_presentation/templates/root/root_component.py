from presentation.templates.stock.stock_component import StockComponent


class RootComponent:

    __stocks = ''
    __style = ''
    
    def __init__(self, headline, date, version, stocks) -> None:
        self.__headline = headline
        self.__date = date
        self.__version = version
        self.__set_style()
        for stock in stocks:
            if(stock is not None):
                self.__stocks += stock.get_html()

    def __set_style(self):
        self.__style += open('./presentation/templates/root/root_component.css', 'r').read()
        self.__style += '\n\n'
        self.__style += StockComponent.get_css()

    def get_component(self):
        component = open('./presentation/templates/root/root_component.html', 'r').read()
        return component.format(
                style=self.__style,
                headline=self.__headline,
                date=self.__date,
                stocks=self.__stocks,
                version=self.__version
            )


        
        