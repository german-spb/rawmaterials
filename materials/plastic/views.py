from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlasticForm, StockForm
from .models import Plastics, Stocks


def index(requests):
    form = PlasticForm()
    return render(requests, 'index.html', {'form': form})

def create_plastic(request):
    # получаем из данных запроса POST отправленные через форму данные
    code_sbk = request.POST.get("code_sbk", "Undefined")
    name_sbk = request.POST.get("name_sbk", "Undefined")
    code_contractor = request.POST.get("code_contractor", "Undefined")
    name_contractor = request.POST.get("name_contractor", "Undefined")
    price = request.POST.get("price", 0)
    note = request.POST.get("note", "Undefined")
    plast = Plastics(code_sbk=code_sbk, name_sbk=name_sbk, code_contractor=code_contractor, name_contractor=name_contractor, price=price, note=note)
    plast.save()
    plast.instance = None
    return HttpResponse('Записано')


def list_plastic(request):
    object_plastic = Plastics.objects.all()
    plastics = [{'code_sbk': c.code_sbk,
                 'name_sbk': c.name_sbk,
                 'code_contractor': c.code_contractor,
                 'name_contractor': c.name_contractor,
                 'price': c.price,
                 'note': c.note} for c in object_plastic]
    context = {
        'plastics': plastics
    }
    return render(request, 'table.html', context)

def stock(requests):
    form = StockForm()
    return render(requests, 'quantity.html', {'form': form})

def input_stock(request):
    # получаем из данных запроса POST отправленные через форму данные
    cod = request.POST.get('plastic')
    plastics = Plastics.objects.filter(id = cod)
    quantity_3050 = request.POST.get("quantity_3050", 0)
    quantity_2440 = request.POST.get("quantity_2440", 0)
    quantity_4200 = request.POST.get("quantity_4200", 0)
    quantity_rol = request.POST.get("quantity_rol", 0)
    for plastic in plastics:
        quan = Stocks(plastic=plastic, quantity_3050=quantity_3050, quantity_2440=quantity_2440, quantity_4200=quantity_4200, quantity_rol=quantity_rol)
        quan.save()
        quan.instance = None
    return HttpResponse('Записано')

# -------------- Поиск ----------------------

def search(request):
    return render(request, "search.html")

def search_plastic(request):
    code_sbk = request.GET.get('code_sbk', 'Запись не найдена')
    code = Plastics.objects.get(code_sbk = code_sbk)
    object_stock = Stocks.objects.filter(plastic=code)
    stocks = [f'{c.plastic}: {c.quantity_3050}  {c.quantity_2440} {c.quantity_4200} {c.quantity_rol}' for c in object_stock]
    return HttpResponse('<br>'.join(stocks))