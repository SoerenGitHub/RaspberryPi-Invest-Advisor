from utils.mockAccount import MockAccount
from utils.depot import Depot
from utils.watchlist import Watchlist
from utils.stock import Stock
from utils.api import Api
from utils.graph import Graph
from analysis.extrema import Extrema
from analysis.supportLine import supportLine

account = MockAccount()
depot = Depot()
watchlist = Watchlist()
api = Api()

account.add(10000)

microsoft = Stock('Microsoft', api.request_history('RDS-B'))

watchlist.add_stock(microsoft)

extrema_microsoft = Extrema(microsoft.get_history()['Close'])
supportLine_microsoft = supportLine(extrema_microsoft)
microsoft_sline = supportLine_microsoft.determine()

graph_microsoft = Graph(microsoft.get_history()['Close'], microsoft.get_name())
graph_microsoft.draw_down_arrow(extrema_microsoft.determine_max())
graph_microsoft.draw_up_arrow(extrema_microsoft.determine_min())
if(microsoft_sline != 0):
    graph_microsoft.draw_hline(microsoft_sline)
graph_microsoft.show()