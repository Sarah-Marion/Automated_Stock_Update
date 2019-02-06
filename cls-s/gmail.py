import datetime
import smtplib
from email.mime.multipart import MIMEMultipart

# Method that establishes a connect to the Gmail server & sending an email to the designated receiver on my behalf

class Gmail:
    def __init__(self):
        return


    def send_email(self,body):
        try:
            # Authentication for Gmail acc.
            gmail_user = '' # set gmail address
            gmail_password = '' # set gmail app pass


            # Email Config set-up!
            msg = MIMEMultipart('alternative')
            msg.attach(body)
            msg['From'] = '' # set from address
            msg['To'] = '' # set to address
            
            now = datetime.datetime.now()
            msg['Subject'] = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + 'Stock Insights'