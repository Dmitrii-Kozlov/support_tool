from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

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
            'docfile': 'Добавить файл (максимальный размер файла 10МВ)',
        }
    def clean_docfile(self):
        content = self.cleaned_data['docfile']
        if content:
            if content.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_(f'Максимальный размер файла 10МВ {filesizeformat(settings.MAX_UPLOAD_SIZE)}. '
                                              f'Текущий размер {filesizeformat(content.size)}'))
        return content


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
    def clean_docfile(self):
        content = self.cleaned_data['docfile']
        if content:
            if content.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_(f'Максимальный размер файла 10МВ {filesizeformat(settings.MAX_UPLOAD_SIZE)}. '
                                              f'Текущий размер {filesizeformat(content.size)}'))
        return content


class SearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, label='Поиск в заголовке')
    title.widget = forms.TextInput(attrs={'class': 'form-control'})
    # module = forms.IntegerField(required=False, label='Поиск в APN')
    # module.widget = forms.NumberInput(attrs={'class': 'form-control'})
    module = forms.ModelChoiceField(required=False, label='Поиск в APN', queryset=AMOSModule.objects.all())
    # module.widget = ForeignKeyRawIdWidget(Case._meta.get_field("module").remote_field, admin.site),
    module.widget = forms.Select(attrs={'class': 'form-control'})
    active = forms.BooleanField(required=False, label='Поиск только открытых заявок')


# class MyCustomForm(ModelForm):
#     class Meta:
#         model = MyModel
#         widgets = {
#             'field': ForeignKeyRawIdWidget(MyModel._meta.get_field("field_to_rel").rel, admin.site),
#         }