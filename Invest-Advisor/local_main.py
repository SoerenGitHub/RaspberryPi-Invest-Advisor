from analysis.rsline.rsline_leverage import RSLineLeverage
from analysis.rsline.rsline_simulation import RSLineSimulation
from utils.mail import Mail
from utils.mockAccount import MockAccount
from utils.depot import Depot
from utils.watchlist import Watchlist
from utils.stock import Stock
from utils.api import Api
from utils.graph import Graph
from analysis.extrema.extrema import Extrema
from analysis.rsline.rsline_analysis import RSLineAnalysis

api = Api()

stock = Stock('Microsoft', api.request_history('DAI.DE'))
rsline_simulation = RSLineSimulation(stock.get_history()['Close'], 1000, 4, 4, 30, 20)