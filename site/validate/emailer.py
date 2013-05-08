import smtplib
from email.mime.text import MIMEText

def send(TO, amount, code):

    FROM = 'bitcoinspring@gmail.com'
    passwd = 'secret'
    
    BODY = 'Hello,\n\nYour recent transaction - for a ${0} Amazon gift card - has reached six (6) confirmations!\n\n'.format(amount)
    BODY += 'Your Amazon giftcard code is as follows: ' + code + '\n\nThank you for shopping with us.\n\n'
    BODY += '---\nBITCOIN SPRING\n---'

    MESSAGE = MIMEText(BODY)
    MESSAGE['Subject'] = 'BITCOIN SPRING --- ORDER SUCCESSFUL'
    MESSAGE['From'] = FROM
    MESSAGE['To'] = TO
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(FROM, passwd)
    s.sendmail(FROM, [TO], MESSAGE.as_string()) 


