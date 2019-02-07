from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader

# Creating the connection to the Gmail server and send the email

class Builder:
    def __init__(self):
        return

    def build_template(self, symbols, summary, articles, venture_name, exchange):
        #Using jinja2 to build email body
        try:
            file_loader = FileSystemLoader('temps')
            env = Environment(loader = file_loader)
            temp = env.get_template('email.html')
            
            # Building jinja2 temp from /temps/email.html
            output = temp.sender(symbols = symbols, summary = summary, articles = articles, venture_name = venture_name, exchange = exchange)

            body = MIMEText(output, 'html')
            return body

        except Exception as e:

            print(str(e))