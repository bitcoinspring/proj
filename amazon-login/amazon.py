import cookielib
import urllib, urllib2
import httplib

httplib.HTTPConnection.debuglevel = 1

cj = cookielib.MozillaCookieJar('amazon.cookies')
cj.load()
form_opener = urllib2.build_opener(
    urllib2.HTTPCookieProcessor(cj),
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=1),
    urllib2.HTTPSHandler(debuglevel=1),
)
form_opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(form_opener)


USERNAME = 'user'
PASSWORD = 'pass'
params = urllib.urlencode({'email': USERNAME, 'password': PASSWORD})

url = 'https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dgno_signout%26signIn%3D1%26useRedirectOnSuccess%3D1'

req = urllib2.Request(url, params)
response = form_opener.open(req)
response = form_opener.open(req)

path = '/media/sdk1/home/impaired/www/donaldgeddes.com/public_html/amazon.html'

with open(path, 'w') as f:
    f.write(response.read())

print 'Done'
print cj
cj.save()
