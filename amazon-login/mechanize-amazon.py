from mechanize import Browser
from cookielib import LWPCookieJar

url = 'https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fie%3DUTF8%26ref_%3Dgno_yam_ya'

cj = LWPCookieJar()

b = Browser()
b.set_cookiejar(cj)

b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)

b.set_debug_http(True)
b.set_debug_redirects(True)
b.set_debug_responses(True)

b.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

b.open(url)
b.select_form(name = 'signIn')

email = 'email here'
password = 'pass here'

b.form['email'] = email
b.form['password'] = password

req = b.submit()

print req
