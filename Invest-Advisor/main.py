from models import Stock
from core import Mail
from presentation import  RootComponent
from utils import Timer
import datetime
import os

mails = [
    'Arnes-mail@web.de',
    'soerens@hotmail.de',
    'hanna.schnell@gmx.de',
    'johanneswitte@gmx.net',
    'm.warneke17@gmx.de'
]

while True:

    if(datetime.date.day == 1):
        os.remove('temp')
        
    Timer().set_timer(7, 30)

    stocks = [
        Stock('BYD', 'BY6.F'),
        Stock('Microsoft', 'MSFT.MI'),
        Stock('Aqua Metals', 'AQK.F'),
        Stock('Apple', 'APC.F'),
        Stock('AMS', 'DQW1.DE'),
        Stock('Square', 'SQ3.F'),
        Stock('Alphabet', 'GOOGL.MI'),
        Stock('Standard Lithium', 'S5L.F'),
        Stock('MERCK', 'MRK.DE'),
        Stock('Ynvisible Interactive', '1XNA.F'),
        Stock('Texas Instruments', 'TII.F'),
        Stock('3D Systems', 'SYV.DE'),
        Stock('Unilever', 'UNA.AS'),
        Stock('Allianz', 'ALV.DE'),
        Stock('Aurora Cannabis', '21P1.F'),
        Stock('Bayer', 'BAYN.DE'),
        Stock('Encavis', 'ECV.DE'),    
    ]
    
    stock_components = []
    for stock in stocks:
        stock_components.append(stock.create_component())
    root_component = RootComponent('Aktien Chart-Analyse', str(datetime.date.today()), 'Alpha 1.0', stock_components)

    for mail_address in mails:
        mail = Mail(mail_address)
        for stock in stocks:
            if(stock.get_graph_image() is not None):
                mail.addImage(stock.get_graph_image(), stock.get_symbol())
        mail.addHtml(root_component.get_component())
        mail.send()
