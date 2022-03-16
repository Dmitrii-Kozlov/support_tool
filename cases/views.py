from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .forms import CaseForm
from .models import Case


class CaseListView(View):
    template_name = 'cases/list.html'

    def get(self, request):
        qs = Case.objects.all()
        context = {
            'items': qs
        }
        return render(request, template_name=self.template_name, context=context)


class CaseDetailView(View):
    template_name = 'cases/detail.html'

    def get(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        context = {
            'item': case
        }
        return render(request, template_name=self.template_name, context=context)


class CaseCreateView(View):
    template_name = 'cases/create.html'

    def get(self, request):
        form = CaseForm()
        context = {
            'form': form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.author = request.user
            case.save()
            return redirect(case.get_absolute_url())
        context = {
            'form': form
        }
        return render(request, template_name=self.template_name, context=context)