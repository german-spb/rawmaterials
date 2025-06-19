from django import forms
from django.forms import inlineformset_factory
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

class UploadFileForm(forms.Form):
    file = forms.FileField()


class PlasticUpdateForm(forms.Form):
    code_sbk = forms.CharField(label="Код СБК", required=True)
    name_sbk = forms.CharField(label="Название СБК", required=False)
    code_contractor = forms.CharField(label="Код поставщика", required=False)
    name_contractor = forms.CharField(label="Название поставщика", required=False)
    price = forms.DecimalField(label="Цена", required=False)
    note = forms.CharField(widget=forms.Textarea, required=False)

    # class Meta:
    #     model = Stocks
    #     fields = ['plastic']
    #     labels = {
    #         'plastic': 'Пластик:',
    #     }

