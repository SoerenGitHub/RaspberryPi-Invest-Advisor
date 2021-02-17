from utils.mail import Mail
from utils.mockAccount import MockAccount
from utils.depot import Depot
from utils.watchlist import Watchlist
from utils.stock import Stock
from utils.api import Api
from utils.graph import Graph
from analysis.extrema import Extrema

account = MockAccount()
depot = Depot()
watchlist = Watchlist()
api = Api()
mail = Mail(['soerens@hotmail.de'])

mail.send()

account.add(10000)

microsoft = Stock('Microsoft', api.request_history('RDS-B'))

watchlist.add_stock(microsoft)

extrema_microsoft = Extrema(microsoft.get_history()['Close'])

graph_microsoft = Graph(microsoft.get_history()['Close'], microsoft.get_name())
graph_microsoft.draw_down_arrow(extrema_microsoft.determine_max())
graph_microsoft.draw_up_arrow(extrema_microsoft.determine_min())
graph_microsoft.show()