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

account.add(10000)

microsoft = Stock('Microsoft', api.request_history('RDS-B'))

watchlist.add_stock(microsoft)

extrema_microsoft = Extrema(microsoft.get_history()['Close'])

