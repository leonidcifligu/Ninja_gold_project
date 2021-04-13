from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'amount' not in request.session:
        request.session['amount']=0
    if 'activities' not in request.session:
        request.session['activities']=[] 
    return render(request, 'index.html')

def process_money(request,location):
    amount = 0
    if location == 'Farm':
        amount=random.randint(10, 21)
    elif location == 'Cave':
        amount=random.randint(5, 11)
    elif location == 'House':
        amount=random.randint(2, 6)
    elif location == 'Casino':
        amount=random.randint(-50, 51)

    request.session['amount'] +=amount
    if amount > 0:
        request.session['activities'].append (f"Yuuupii you won {amount} gold") 
    else:
        request.session['activities'].append (f"Ouch you lost {amount} gold")

    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['amount'] = 0
        request.session['activities'] = []
    return redirect('/')

