from django import forms
from django.forms import inlineformset_factory
from .models import Plastics, Stocks, Chipboard
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

class ChipboardUpdateForm(forms.Form):
    thickness = forms.CharField(label="Наименование", required=True)
    form = forms.CharField(label="Формат", required=True)
    aqua = forms.CharField(label="Влагостойкость", required=True)
    sort = forms.CharField(label="Сорт", required=True)
    unit = forms.CharField(label="Единица изм.", required=False)
    price = forms.DecimalField(label="Цена", required=False)


