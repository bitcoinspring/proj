import urllib, urllib2
import json
from pprint import pprint

o = urllib2.build_opener(urllib2.HTTPHandler)
o.addheaders = [('Authorization', '33e600d1a962034011003c2308ef7bdb9c56a32d')]

def agents():
    url = 'http://www.bitcoinmonitor.net/api/v1/agent/'
    response = o.open(url)
    return json.loads(response.read())

def get_id(name):
    data = agents()
    for key in data:
        if key['name'] == name:
            return key['id']  

def create(name, address):
    url = 'http://www.bitcoinmonitor.net/api/v1/agent/'
    params = {
                'name': name,
                'watch_type': '3',
                'addresses': address,
             }
    params = urllib.urlencode(params)
    response = o.open(url, params)
    return response.read()

def notify(name):
    id = get_id(name)
    url = 'http://www.bitcoinmonitor.net/api/v1/agent/{0}/notification/url/'.format(id)
    for conf_num in [0,1,2,3,4,5,6]:
        params = {
                    'req_confirmations': conf_num,
                    'url': 'http://bitcoinspring.com:4000/validate/',
                 }
        params = urllib.urlencode(params)
        response = o.open(url, params)
    return 'Success'

def delete(name):
    id = get_id(name)
    url = 'http://www.bitcoinmonitor.net/api/v1/agent/{0}/'.format(id)
    request = urllib2.Request(url)
    request.get_method = lambda: 'DELETE'
    response = o.open(request)
    return response.read()

delete('validate')
create('validate', '17UJbo6TFtCWopvQTY89yD2xSWBhgxuL6k')
print notify('validate')
