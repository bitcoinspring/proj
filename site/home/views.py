from django.http import HttpResponse
from django.shortcuts import render
from home.forms import OrderForm
from django.utils import timezone
import agent, emailer

PWD = '/media/sdk1/home/impaired/private/projects/bitcoinspring/home/'
address = '17UJbo6TFtCWopvQTY89yD2xSWBhgxuL6k'

def home(r):
    f = OrderForm()
    return render(r, 'home/index.html', {'form': f})

def order(r):

    # Ascertains generic client info re POST
    ip = r.META['REMOTE_ADDR']
    tz = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    # Checks POST method
    if r.method == 'POST':

        # Instantiate form
        f = OrderForm(r.POST)

        # Checks if form submitted was valid
        if f.is_valid():
            data = r.POST
            username = data['username']
            email = data['email']
            amount = data['amount']

            # For debugging purposes
            print '\n'
            print 'Successful POST'
            print '--> Date/Time: ' + tz
            print '--> IP: ' + ip
            print '--> Data'
            print '    --> Username: ' + username
            print '    --> Email address: ' + email
            print '    --> GC Amount: ' + amount
            print '\n'
            
            agent.create('camus')

            # Fetch Amazon GC code
            with open(PWD+'codes','r') as f:
                codes = f.read().splitlines()
                if len(codes) == 0:
                    return HttpResponse('Order failed.')
                code = codes[0]
                del codes[0]
                codes = '\n'.join(codes)
                f.close()

            # Rewrite code file to reflect the removed GC code
            with open(PWD+'codes', 'w') as f:
                f.write(codes)
                f.close()
    
            # Sends GC code to customer
            # email = their email address
            # username = their chosen username
            # amount = the GC amount
            # code = Amazon GC code
            emailer.send(email, username, amount, code)

            return HttpResponse('Order success!')
            

        else:
            # For debugging purposes
            print '\n'
            print 'Unsuccessful POST'
            print '--> Date/Time: ' + tz
            print '--> IP: ' + ip
            print '\n'

            # Tra-la-fucking-la
            return HttpResponse('<!--Of the wide world I stand alone, and think, / Till Love and Fame to nothingness do sink.-->')
