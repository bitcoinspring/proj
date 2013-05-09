from django.shortcuts import render
from django.http import HttpResponse
from sandbox.forms import OrderForm
import json 

emails = ["asdf@asdf.com", "you@suck.com"]

def post(r):
    if r.method == 'POST':
        if r.META['HTTP_REFERER'] == 'http://donaldgeddes.com:4000/sandbox/':
            return HttpResponse(r.META['HTTP_REFERER'])
    else:
        return HttpResponse('Go love yourself')

def play(r):
    f = OrderForm()
    return render(r, 'sandbox/index.html', {'form': f, 'emails': json.dumps(emails)})
