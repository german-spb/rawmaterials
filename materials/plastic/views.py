from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import PlasticForm, StockForm, UploadFileForm
from .models import Plastics, Stocks, Result
import pandas as pd


def home(request):
    return render(request, "navbar.html")



def code_entry(requests):
    form = PlasticForm()
    return render(requests, 'code_entry.html', {'form': form})

def create_plastic(request):
    # получаем из данных запроса POST отправленные через форму данные
    code_sbk = request.POST.get("code_sbk", "Undefined")
    print(code_sbk)
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
    plastics = Plastics.objects.all()
    return render(request, 'table.html', {'plastics' : plastics})

def list_quantity(request):
    stocks_object = Stocks.objects.all()
    stocks = [{
        'plastic': c.plastic,
        'quantity_3050': c.quantity_3050,
        'quantity_2440': c.quantity_2440,
        'quantity_4200': c.quantity_4200,
        'quantity_rol': c.quantity_rol,
        'total': c.quantity_3050 + c.quantity_2440 + c.quantity_4200} for c in stocks_object]
    context = {
        'stocks': stocks
    }
    return render(request, 'search.html', context)


# -------------------- Запись количества ----------------

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
        values_for_update = {'plastic': plastic, 'quantity_3050' : quantity_3050, 'quantity_2440' : quantity_2440, 'quantity_4200' :quantity_4200, 'quantity_rol' :quantity_rol}
        quan = Stocks.objects.update_or_create(id=cod, defaults=values_for_update)
    return HttpResponse('Записано')

# -------------- Поиск ----------------------

def search(request):
    return render(request, "search_form.html")

def search_plastic(request):
    code_sbk = request.GET.get('code_sbk', 'Запись не найдена')
    plastics_object = Plastics.objects.filter(code_sbk=code_sbk)
    plastics = [{
        'code_sbk': c.code_sbk,
        'name_sbk': c.name_sbk,
        'code_contractor': c.code_contractor,
        'name_contractor': c.name_contractor,
        'price': c.price,
        'note': c.note} for c in plastics_object]
    try:
        code = Plastics.objects.get(code_sbk = code_sbk)
        stocks_object = Stocks.objects.filter(plastic=code).order_by('-id')[:1]
        stocks = [{
            'plastic': c.plastic,
            'quantity_3050': c.quantity_3050,
            'quantity_2440': c.quantity_2440,
            'quantity_4200': c.quantity_4200,
            'quantity_rol': c.quantity_rol,
            'total': c.quantity_3050 + c.quantity_2440 + c.quantity_4200} for c in stocks_object]
        context = {
            'stocks': stocks,
            'plastics': plastics
        }
        return render(request, 'search.html', context)
    except Plastics.DoesNotExist:
        return HttpResponse('<h1>Запись не найдена или неверный код пластика</h1>')

# def search_plastic(request):
#     code_sbk = request.GET.get('code_sbk', 'Запись не найдена')
#     try:
#         code = Plastics.objects.get(code_sbk = code_sbk)
#         stocks_object = Stocks.objects.filter(plastic=code).order_by('-id')[:1]
#         stocks = [{
#             'plastic': c.plastic,
#             'quantity_3050': c.quantity_3050,
#             'quantity_2440': c.quantity_2440,
#             'quantity_4200': c.quantity_4200,
#             'quantity_rol': c.quantity_rol,
#             'total': c.quantity_3050 + c.quantity_2440 + c.quantity_4200} for c in stocks_object]
#         context = {
#             'stocks': stocks
#         }
#         return render(request, 'search.html', context)
#     except Plastics.DoesNotExist:
#         return HttpResponse('<h1>Запись не найдена или неверный код пластика</h1>')

# ---------------- Удаление ------------------

def form_delete(request):
  return render(request, "delete.html")

def delete(request):
    code_sbk = request.GET.get('code_sbk', 'Запись не найдена')
    code = Plastics.objects.get(code_sbk=code_sbk)
    Stocks.objects.filter(plastic=code).delete()
    Plastics.objects.get(code_sbk=code_sbk).delete()
    return HttpR0esponse('Запись удалена!')

def delete_stock(request):
    Stocks.objects.all().delete()
    return HttpResponse('Таблица запасов пластика удалена')

# ------------------Загрузка количества через excel файл ---------------

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                try:
                    created = Stocks.objects.update_or_create(
                        # code_sbk = row['plastic'],
                        plastic= Plastics.objects.get(code_sbk= row['plastic']),
                        quantity_3050=row['quantity_3050'],
                        quantity_2440=row['quantity_2440'],
                        quantity_4200=row['quantity_4200'],
                        quantity_rol=row['quantity_rol'],
                    )
                    # messages.success(request, f'Successfully imported files')
                except Plastics.DoesNotExist:
                    return HttpResponse(f'<h1>неверный код пластика: {row['plastic']}</h1>')
        return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

#-------------- Загрузка кодов пластика через excel файл ---------------

def upload_code(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():

                created = Plastics.objects.update_or_create(
                    code_sbk = row['plastic'],
                )
                if created:
                    messages.success(request, f'Successfully imported files')
                else:
                    messages.warning(request, f'files already exists')
            return redirect('upload_code')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# --------------- Обработка файла RESULT по поставщику ---------------

def upload_result(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                code = Plastics.objects.get(code_sbk=row['plastic'])
                print(code)
                plastics = Stocks.objects.filter(plastic=code)
                for plastic in plastics:
                    values_for_update = {
                        'plastic': row['plastic'],
                        'quantity_sheet': plastic.quantity_3050+plastic.quantity_2440+plastic.quantity_4200,
                        'quantity_rol': plastic.quantity_rol,
                        'total': plastic.quantity_3050+plastic.quantity_2440+plastic.quantity_4200+plastic.quantity_rol
                    }
                    Result.objects.update_or_create(plastic=row['plastic'], defaults=values_for_update)

            return redirect('upload_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def list_result(request):
    plastics = Result.objects.all()
    return render (request, 'result.html', {'plastics' : plastics})

def delete_result(request):
    Result.objects.all().delete()
    return HttpResponse ('Таблица удалена')

# --------------- Запись в excel файл -------------

def to_excel(request):
    data = Result.objects.all().values()
    df = pd.DataFrame(data)
    df.to_excel("output.xlsx")
    return HttpResponse('Файл EXCEL создан')