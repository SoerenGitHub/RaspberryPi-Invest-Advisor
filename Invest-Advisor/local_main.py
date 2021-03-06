
from mail.templates.root.root_component import RootComponent
from mail.templates.stock.stock_component import StockComponent
from mail.mail import Mail


stocka_component = StockComponent('test1', 'TEST1', 'https://cdn.shortpixel.ai/spai/w_995+q_glossy+ret_img+to_webp/https://www.sharpsightlabs.com/wp-content/uploads/2019/02/simple-matplotlib-line-chart_TSLA-stock-price.png')
stockb_component = StockComponent('test2', 'TEST2', 'https://cdn.shortpixel.ai/spai/w_995+q_glossy+ret_img+to_webp/https://www.sharpsightlabs.com/wp-content/uploads/2019/02/simple-matplotlib-line-chart_TSLA-stock-price.png')

stocks = [stocka_component, stockb_component]

root_component = RootComponent('testheadline', '07.07.2021', 'Alpha 1.0', stocks)

mail = Mail(['soerens@hotmail.de'])
mail.addHtml(root_component.get_component())
mail.send()
