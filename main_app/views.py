from django.shortcuts import render
from .models import *

def start(request):
    items = All_items.objects.all()

    categories = Categories.objects.all()

    return render(request, 'main_app/index.html', {'item': items, 'categories': categories })

def one_item(request, id:int):
    items = All_items.objects.get(id=id)

    return render(request,'main_app/des.html', { 'item': items })

