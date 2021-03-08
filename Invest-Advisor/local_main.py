import datetime
from models import Stock
from core import Mail
from presentation import  RootComponent
from utils import Timer

mails = [
    'schuba.s_dev@outlook.com',
    'soerens@hotmail.de'
]


for mail in mails:
    mail = Mail(mail)

    stocks = [
        Stock('TUI', 'TUI1.DE').create_component(mail), 
        Stock('Microsoft', 'MSFT').create_component(mail)
    ]

    root_component = RootComponent('Aktien Chart-Analyse', str(datetime.datetime.now()), 'Alpha 1.0', stocks)
    mail.addHtml(root_component.get_component())
    mail.send()
