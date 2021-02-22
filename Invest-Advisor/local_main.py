from utils.graph import Graph
from utils.simplifier import Simplifier
from utils.stock import Stock
from utils.api import Api
from analysis.rsline.rsline_simulation import RSLineSimulation
from analysis.extrema.extrema import Extrema

api = Api()

stock = Stock('Test','egal',  api.request_history('BYD'))
rsline_simulation = RSLineSimulation(stock.get_history()['Close'], 2300, 3, 3, 30)

#prediction = LSTMPredictionKI(stock, 50)