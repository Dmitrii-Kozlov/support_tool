from django.forms import ModelForm, Textarea, TextInput, Select
from .models import Case


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'module']
        widgets = {
            'description': Textarea(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'module': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Краткое описание',
            'description': 'Описание',
            'module': 'Модуль'
        }