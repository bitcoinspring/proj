import smtplib

def send(TO, amount, code):

    TO = str(TO)
    FROM = 'bitcoinspring@gmail.com'
    passwd = 'obfuscated'
    
    SUBJECT = 'BITCOIN SPRING --- ORDER SUCCESSFUL'
    BODY = 'Hello,\n\nYour recent transaction - for a ${0} Amazon gift card - has reached six (6) confirmations!\n\n'.format(amount)
    BODY += 'Your Amazon giftcard code is as follows: ' + code + '\n\nThank you for shopping with us.\n\n'
    BODY += '---\nBITCOIN SPRING\n---'
    MESSAGE = 'Subject: {0}\n\n{1}'.format(SUBJECT, BODY)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(FROM, passwd)
    s.sendmail(FROM, TO, MESSAGE) 


