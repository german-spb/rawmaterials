from django import forms
from .models import Plastics, Stocks

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