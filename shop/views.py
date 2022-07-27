from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item, Purchase


def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')


def list_item(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'item_list': items})


def detail_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {'item': item}
    return render(request, 'detail.html', context)

