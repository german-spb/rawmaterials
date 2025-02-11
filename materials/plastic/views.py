from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlasticForm
from .models import Plastics


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