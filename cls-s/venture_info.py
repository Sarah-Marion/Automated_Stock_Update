import requests

class Info:
    """
    Class that makes a GET request to the IEX API
    """
    def __init__(self):
        return

    def get_summary(self, symbol, stock_url):
        """
        Returns the summary of the latest article that mentions that particular stock from IEX API endpoint
        """
        try:
            # Fetch summary of latest article
            response = requests.get(stock_url + symbol + '/news/last/1')
            json = response.json()
            return json [0]['summary']
        
        except Exception as e:
            
            print(str(e))


    def get_articles(self, symbol, stock_url):
        """
        Returns the link to the latest article that mentions that particular stock from IEX API endpoint
        """
        try:
            # Fetch latest article
            response = requests.get(stock_url + symbol + '/news/last/1')
            json = response.json()
            return json [0]['url']

        except Exception as e:

            print(str(e))


    def get_venture_name(self, symbol, stock_url):
        """
        Returns the venture name based on that stock symbol from IEX API endpoint
        """
        try:
            # Fetch venture name
            response = requests.get(stock_url + symbol + '/company')
            json = response.json()
            return json['ventureName']

        except Exception as e:

            print(str(e))

    def get_exchange(self, symbol, stock_url):
        """
        Returns the stock exchange that stock belongs to from IEX API endpoint
        """
        try:
            # Fetch the stock exchange belongs to
            response = requests.get(stock_url + symbol + '/company')
            json = response.json()
            return json['exchange']

        except Exception as e:

            print(str(e))
