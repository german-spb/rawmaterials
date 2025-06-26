from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django_filters.conf import settings
from django.contrib.auth.models import User
from .forms import PlasticForm, StockForm, UploadFileForm, PlasticUpdateForm, ChipboardForm, ChipboardUpdateForm
from .models import Plastics, Stocks, Result, Chipboard
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import os
from django.urls import path
from django.conf import settings
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('home')

    # Render the login page template (GET request)
    return render(request, 'login.html')


def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)

        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')

        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # Set the user's password and save the user object
        user.set_password(password)
        user.save()

        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')

    # Render the registration page template (GET request)
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, "navbar1.html")

@login_required
def plastic(request):
    return render(request, "navbar.html")

@login_required
def code_entry(requests):
    form = PlasticForm()
    return render(requests, 'code_entry.html', {'form': form})

@login_required
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
    dt = stocks_object.values('created_at').last()['created_at'].strftime("%d-%m-%Y %H:%M")

    return render(request, 'search_list_quantity.html', {'stocks': stocks, 'dt': dt})


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

# ------------------Обновление кода ДБСП-----------------
def input_update_code(request):
    form = PlasticUpdateForm()
    return render(request, 'update_code.html', {'form': form})

def input_update_code_fields(request):
    code = request.GET.get('code_sbk')
    cur_objects = Plastics.objects.filter(code_sbk=code)
    plastics = [{
        'code_sbk': c.code_sbk,
        'name_sbk': c.name_sbk,
        'code_contractor': c.code_contractor,
        'name_contractor': c.name_contractor,
        'price': c.price,
        'note': c.note} for c in cur_objects]
    cur_name_sbk  = plastics[0]['name_sbk']
    cur_code = plastics[0]['code_contractor']
    cur_name_contractor = plastics[0]['name_contractor']
    cur_price = plastics[0]['price']
    cur_note = plastics[0]['note']
    if request.GET.get("name_sbk"):
        name_sbk = request.GET.get("name_sbk")
    else: name_sbk = cur_name_sbk
    if request.GET.get("code_contractor"):
        code_contractor = request.GET.get("code_contractor")
    else: code_contractor = cur_code
    if request.GET.get("name_contractor"):
        name_contractor = request.GET.get("name_contractor")
    else: name_contractor = cur_name_contractor
    if request.GET.get("price"):
        price = request.GET.get("price")
    else: price = cur_price
    if request.GET.get("note"):
        note = request.GET.get("note")
    else: note = cur_note
    Plastics.objects.filter(code_sbk=code).update(name_sbk=name_sbk, code_contractor=code_contractor, name_contractor=name_contractor, price=price, note=note)
    return redirect(request.META.get('HTTP_REFERER')) # возврат на предыдущую страницу


# -------------- Поиск --------------------------------

def search(request):
    return render(request, "search_form.html")

def search_plastic(request):
    form = PlasticUpdateForm()
    code_sbk = request.GET.get('code_sbk')
    plastics_object = Plastics.objects.filter(code_sbk__iexact = code_sbk)
    plastics = [{
        'code_sbk': c.code_sbk,
        'name_sbk': c.name_sbk,
        'code_contractor': c.code_contractor,
        'name_contractor': c.name_contractor,
        'price': c.price,
        'note': c.note} for c in plastics_object]
    try:
        code = Plastics.objects.get(code_sbk__iexact  = code_sbk)
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
            'plastics': plastics,
            'form' : form
        }
        return render(request, 'search.html', context)
    except Plastics.DoesNotExist:
        return HttpResponse('<h1>Запись не найдена или неверный код пластика</h1>')


# ---------------- Удаление ------------------

def form_delete(request):
  return render(request, "delete.html")

def delete(request):
    code_sbk = request.GET.get('code_sbk', 'Запись не найдена')
    code = Plastics.objects.get(code_sbk=code_sbk)
    Stocks.objects.filter(plastic=code).delete()
    Plastics.objects.get(code_sbk=code_sbk).delete()
    return HttpResponse('Запись удалена!')

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

                        plastic= Plastics.objects.get(code_sbk= row['plastic']),
                        quantity_3050=row['quantity_3050'],
                        quantity_2440=row['quantity_2440'],
                        quantity_4200=row['quantity_4200'],
                        quantity_rol=row['quantity_rol'],
                    )
                    # messages.success(request, f'Successfully imported files')
                except Plastics.DoesNotExist:
                    return HttpResponse(f'<h1>неверный код пластика: {row["plastic"]}</h1>')
        return redirect('home')
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
            n = file.name
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                try:
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
                except Plastics.DoesNotExist:
                    return HttpResponse(f'<h1>Пластик с кодом {row["plastic"]} отсутствует на складе</h1>')
            # redirect('upload_file')
            return HttpResponse(f'<h1>Таблица поставщика {n} заполнена</h1><br><h2><a href="/">В начало</a></h2>')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form })

def list_result(request):
    plastics = Result.objects.all()
    return render (request, 'result.html', {'plastics' : plastics})

def delete_result(request):
    Result.objects.all().delete()
    return HttpResponse ('Таблица поставщика удалена')

# --------------- Запись в excel файл -------------

def to_excel(request):
    data = Result.objects.all().values()
    df = pd.DataFrame(data)
    df.to_excel("plastic/static/output.xlsx", index=False)
    return HttpResponse('<h2><a href="/static/output.xlsx">Скачать Excel файл поставщика</a></h2>')

#--------------------Скачивание файла с сервера -------------


def download_file(request, filename):
    file_path = os.path.join(settings.STATIC_ROOT, 'files', filename)
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = FileResponse(file)
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        return HttpResponse("File not found", status=404)

#===================================== ДСП =================================================

def chipboard(request):
    chipboars = Chipboard.objects.all()
    return render(request, 'chipboard.html', {'chipboards': chipboars})

def chipboard_form(request):
    form_create = ChipboardForm()
    form_update = ChipboardUpdateForm
    chipboars = Chipboard.objects.all()
    return render(request, "chipboard_form.html", {'form': form_create, 'form_update': form_update, 'chipboards': chipboars})

def chipboard_create(request):
    thickness = request.POST.get('thickness')
    format = request.POST.get('format')
    aqua = request.POST.get('aqua')
    sort = request.POST.get('sort')
    unit = request.POST.get('unit')
    price = request.POST.get('price')
    chipboard = Chipboard(thickness=thickness, format=format, aqua=aqua, sort=sort, unit=unit, price=price)
    chipboard.save()
    # return HttpResponse('Записано')
    return redirect(request.META.get('HTTP_REFERER'))

def chipboard_update(request):
    thickness = request.GET.get('thickness')
    format = request.GET.get('format')
    aqua = request.GET.get('aqua')
    sort = request.GET.get('sort')
    chip_objects = Chipboard.objects.filter(thickness=thickness)
    print(chip_objects)
    chipboards = [{
        'thickness': c.thickness,
        'format': c.format,
        'aqua': c.aqua,
        'sort': c.sort,
        'unit': c.unit,
        'price': c.price} for c in chip_objects]
    print(chipboards)
    cur_thickness = chipboards[0]['thickness']
    cur_format = chipboards[0]['format']
    cur_aqua = chipboards[0]['aqua']
    cur_sort = chipboards[0]['sort']
    cur_unit = chipboards[0]['unit']
    cur_price = chipboards[0]['price']
    if request.GET.get("thickness"):
        thickness = request.GET.get("thickness")
    else: thickness = cur_thickness
    if request.GET.get("format"):
        format = request.GET.get("format")
    else: format = cur_format
    if request.GET.get("aqua"):
        aqua = request.GET.get("aqua")
    else: aqua = cur_aqua
    if request.GET.get("unit"):
        unit = request.GET.get("unit")
    else: unit = cur_unit
    if request.GET.get("price"):
        price = request.GET.get("price")
    else: price = cur_price
    Chipboard.objects.filter(thickness=thickness, format=format, aqua=aqua,sort=sort).update(thickness=thickness, format=format, aqua=aqua,sort=sort, unit=unit, price=price)
    return redirect(request.META.get('HTTP_REFERER'))


