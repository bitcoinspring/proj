from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import emailer, giftcard

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
        
        # Ensure transaction data is present
        if 'signed_data' in transaction:
            
            # Hunting and gathering
            transaction = transaction['signed_data']
            confirmations = transaction['confirmations']
            address = transaction['address']
           
            # Update user model with new confirmation number
            # This number will be fetched when rendering /status/ page
            # Note: the model stuff is in pseudo code because it hasn't been made yet
            user(address).confirmations(confirmations)
           
            # Complete transaction if confirmations == 6
            if confirmations == 6:
                # Update user model 
                user(address).complete(True)
                # Send final email
                username = user(address).username
                email = user(address).email
                amount = user(address).amount
                code = giftcard.get(amount)
                message = emails.complete
                emailer.send(email, username, amount, code)  


        # This is what client web browsers see
        return HttpResponse('<!--Idleness is fatal only to the mediocre man.-->') 
    

    # (If there's no POST, you still need to resopnd with something)
    return render(r, 'validate/index.html', {})
