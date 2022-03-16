from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
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
