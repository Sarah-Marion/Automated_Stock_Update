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
            gmail_user = 'roxyfoxerme@gmail.com' 
            gmail_password = 'synagen123' 


            # Email Config set-up!
            msg = MIMEMultipart('alternative')
            msg.attach(body)
            msg['From'] = 'roxyfoxerme@gmail.com' 
            msg['To'] = 'mumeronick@gmail.com' # set to address
            
            now = datetime.datetime.now()
            msg['Subject'] = str(now.day) + '-' + str(now.month) + '-' + str(now.year) + 'Stock Insights'

            # Email sending
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.close()

        except Exception as e:

            print(str(e))
            