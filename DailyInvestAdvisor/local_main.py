from process.process import Process
from a_data.stock import Stock


stocks = [
    Stock('BYD', 'BY6.F')
]

for stock in stocks:
    stock_process = Process(stock)
    stock_process.start()
    stock_process