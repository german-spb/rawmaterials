from django import forms
from .models import Plastics

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