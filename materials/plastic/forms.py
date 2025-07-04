from django import forms
from django.forms import inlineformset_factory
from .models import Plastics, Stocks, Chipboard, Glue
from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class PlasticForm(forms.ModelForm):
    class Meta:
        model = Plastics
        fields = '__all__'
        labels = {
            'code_sbk': 'Код СБК:',
            'name_sbk': 'Название СБК:',
            'code_contractor': 'Код поставщика:',
            'name_contractor': 'Название поставщика:',
            'price': 'Цена, м2:',
            'note': 'Примечание:',
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = '__all__'
        labels = {
            'plastic': 'Пластик:',
            'quantity_3050': 'Листы 3050, м2:',
            'quantity_2440': 'Листы 2440, м2:',
            'quantity_4200': 'Листы 4200, м2:',
            'quantity_rol': 'Рулоны, м2:',
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()


class PlasticUpdateForm(forms.Form):
    code_sbk = forms.CharField(label="Код СБК", required=True)
    name_sbk = forms.CharField(label="Название СБК", required=False)
    code_contractor = forms.CharField(label="Код поставщика", required=False)
    name_contractor = forms.CharField(label="Название поставщика", required=False)
    price = forms.DecimalField(label="Цена", required=False)
    note = forms.CharField(widget=forms.Textarea, required=False)


class ChipboardForm(forms.ModelForm):
    class Meta:
        model = Chipboard
        fields = '__all__'
        labels = {
            'thickness': 'Толщина плиты',
            'format' : 'Формат плиты',
            'aqua' : 'Водостойкость',
            'sort': 'Сорт плиты',
            'unit': 'Единица измерения',
            'price': 'Цена',
        }


class GlueForm(forms.ModelForm):
    class Meta:
        model = Glue
        fields = '__all__'
        labels = {
            'name': 'Название',
            'main': 'Основной',
            'type': 'Тип',
            'supplier': 'Поставщик',
            'pack': 'Упаковка',
            'price': 'Цена',
            'line': 'Линия №'
        }

class GlueForm2(forms.Form):
    name = forms.CharField(label='Название', required=True)
    main = forms.BooleanField(label='Основной', required=False)
    type = forms.CharField(label='Тип', required=True)
    supplier = forms.CharField(label='Поставщик', required=True)
    pack = forms.CharField(label='Упаковка',required=True)
    price = forms.DecimalField(label='Цена', required=True)
    line = forms.CharField(label='Линия', required=True)

