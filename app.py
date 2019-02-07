import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), './cls-s'))
from gmail import Gmail
from venture_info import Info
from temp_builder import Builder

mail = Gmail()
info = Info()
temp = Builder()

stockURL = 'https://api.iextrading.com/1.0/stock/'
symbols = ['AMZN', 'GOOGL', 'AAPL'] # add more stock symbols 
summary = []
articles = []
ventureName = []
exchange = []

try:
    # Fetching latest articles
    for i in symbols:
        summary.append(info.get_summary(i, stockURL))
        articles.append(info.get_articles(i, stockURL))
        ventureName.append((info.get_venture_name(i, stockURL)))
        exchange.append(info.get_exchange(i, stockURL))

    # Jinja2 temp building
    body = temp.build_temp(symbols, summary, articles, ventureName, exchange)

    # Send Email
    mail.send_email(body)

    print('Email sent!')
except Exception as e:

    print(str(e))
