from models import Stock
from core import Mail
from presentation import  RootComponent
from utils import Timer
import datetime

mails = [
    'Arnes-mail@web.de',
    'soerens@hotmail.de',
    'hanna.schnell@gmx.de'
]

while True:

    Timer().set_timer(7, 30)

    for mail in mails:
        mail = Mail(mail)

        stocks = [
            Stock('BYD', 'BY6.F').create_component(mail), 
            Stock('Microsoft', 'MSFT.MI').create_component(mail),
            Stock('Aqua Metals', 'AQK.F').create_component(mail),
            Stock('Apple', 'APC.F').create_component(mail),
            Stock('AMS', 'DQW1.DE').create_component(mail),
            Stock('Square', 'SQ3.F').create_component(mail),
            Stock('Alphabet', 'GOOGL.MI').create_component(mail),
            Stock('Standard Lithium', 'S5L.F').create_component(mail),
            Stock('MERCK', 'MRK.DE').create_component(mail),
            Stock('Ynvisible Interactive', '1XNA.F').create_component(mail),
            Stock('Texas Instruments', 'TII.F').create_component(mail),
            Stock('3D Systems', 'SYV.DE').create_component(mail),
            Stock('Unilever', 'UNA.AS').create_component(mail),
            Stock('Allianz', 'ALV.DE').create_component(mail),
        ]

        root_component = RootComponent('Aktien Chart-Analyse', str(datetime.datetime.now()), 'Alpha 1.0', stocks)
        mail.addHtml(root_component.get_component())
        mail.send()
