from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import emailer
import json

@csrf_exempt
def recv(r):
    if r.method == 'POST':

        transaction = json.loads(r.body) # POST data will be JSON

        # For debugging purposes

        print 'Created at: ' + transaction['signed_data']['created']
        print 'Confirmations: ' + str(transaction['signed_data']['confirmations'])

        # Do legwork here - ie. check transaction['confirmations'] and determine 
        # whether or not the gift card should be emailed. Otherwise, there should 
        # be a status page for our customers to view how many confirmations their 
        # tx has received, etc. (That last bit will require quite a bit more work.)

        # This is what client web browsers see
        return HttpResponse('<!--Idleness is fatal only to the mediocre man.-->') 
    

    # (If there's no POST, you still need to resopnd with something)
    return render(r, 'validate/index.html', {})
