import smtplib

def send(TO, code):

    FROM = 'bitcoinspring@gmail.com'
    passwd = 'obfuscated'
    
    SUBJECT = 'BITCOIN SPRING --- ORDER SUCCESSFUL'
    BODY = 'Hello,\n\nYour recent transaction with us has reached six (6) confirmations.\n\n'
    BODY += 'Here is your Amazon giftcard code: ' + code + '\n\nThank you for shopping with Bitcoin Spring\n\n'
    BODY += '---\nBITCOIN SPRING'
    MESSAGE = 'Subject: {0}\n\n{1}'.format(SUBJECT, BODY)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(FROM, passwd)
    s.sendmail(FROM, TO, MESSAGE) 


