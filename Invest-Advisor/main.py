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

account.add(10000)
mail.send()
