from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Item

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    context = {'name': 'Всякие Фигнюшки'}
    return render(request, 'home.html', context)


def about(request):
    context = {'name': 'Anton', 'phone_number': '890211111111', 'email': 'inion@gmail.com'}
    return render(request, 'about.html', context)


def item(request, item_id):
    global items
    result = {}
    for i in items:
        if i['id'] == item_id:
            result['name'] = i['name']
            if i['quantity'] != 0:
                result['quantity'] = i['quantity']
            else:
                result['quantity'] = 'товар отсутствует'
            break
    return render(request, 'item.html', result)


def get_items(request):
    global items
    return render(request, 'items.html', {'items': items})


def fill(request):
    item = Item(name='Молоко', quantity=5)
    item.save()
    return HttpResponse('Успешно')


def create_item(request):
    item = Item(name='Молоко', quantity=5, price=500)
    item.save()
    result = f'{item.name} Количество {item.quantity} Цена {item.price}'
    return HttpResponse(result)


def read_item(request, item_id):
    item = Item.objects.filter(pk=item_id).first()  # pk - это primary key
    result = f'{item.name} Количество {item.quantity} Цена {item.price}'
    return HttpResponse(result)


def update_item(request, item_id):
    item = Item.objects.filter(pk=item_id).first()
    item.name = 'Гвозди'
    item.save()
    result = f'{item.name} Количество {item.quantity} Цена {item.price}'
    return HttpResponse(result)


def delete_item(request, item_id):
    item = Item.objects.filter(pk=item_id).first()  # pk - это primary key
    item.delete()
    return HttpResponse('Успешно')
