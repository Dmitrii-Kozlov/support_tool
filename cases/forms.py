from django import forms
from .models import Case, Comment, AMOSModule


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'module', 'docfile']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'module': forms.Select(attrs={'class': 'form-control'}),
            'docfile': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Краткое описание',
            'description': 'Описание',
            'module': 'Модуль',
            'docfile': 'Добавить файл',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'docfile']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'docfile': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'body': 'Ваш ответ',
            'docfile': 'Добавить файл',
        }


class SearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label='Поиск в описании')
    title.widget = forms.TextInput(attrs={'class': 'form-control'})
    # module = forms.IntegerField(required=False, label='Поиск в APN')
    # module.widget = forms.NumberInput(attrs={'class': 'form-control'})
    module = forms.ModelChoiceField(required=False, label='Поиск в APN', queryset=AMOSModule.objects.all())
    module.widget = forms.Select(attrs={'class': 'form-control'})
    active = forms.BooleanField(required=False, label='Поиск только открытых заявок')

