from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Account

def start(request):

    #can see in dbeaver
    #orm
    a= Account.objects.create(
        amount=10,
        currency = "inr"
    )
    a_fetched = Account.objects.all()
    print(a_fetched)
    return HttpResponse("Hello")