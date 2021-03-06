from graph.graph import Graph
from utils.stock import Stock
from mail.templates.root.root_component import RootComponent
from mail.templates.stock.stock_component import StockComponent
from mail.mail import Mail
from utils.api import Api
from analysis.rsline.rsline_analysis import RSLineAnalysis
from analysis.extrema.extrema import Extrema

api = Api()

microsoft_history = api.request_history('TUI1.DE')
microsoft_stock = Stock('TUI', 'TUI1.DE', microsoft_history['Close'])
microsoft_graph = Graph(microsoft_history['Close'], 'TUI')
microsoft_extrema = Extrema(microsoft_history['Close'], 1)
microsoft_rsline = RSLineAnalysis(microsoft_extrema, 6, 6, 15, microsoft_history['Close'].values[-1])
microsoft_graph.draw_hline(microsoft_rsline.get_price())
microsoft_graph_img = microsoft_graph.save('TUI1.DE', '06.03.2021')
microsoft_component = StockComponent('TUI', 'TUI1.DE', 'cid:tui')

stocks = [microsoft_component]

root_component = RootComponent('Aktien Chart-Analyse', '06.03.2021', 'Alpha 1.0', stocks)

mail = Mail(['soerens@hotmail.de'])
mail.addImage(microsoft_graph_img, 'tui')
mail.addHtml(root_component.get_component())
mail.send()
