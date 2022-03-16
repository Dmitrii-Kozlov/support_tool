from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .forms import CaseForm, CommentForm, SearchForm
from .models import Case


class CaseListView(View):
    template_name = 'cases/list.html'

    def get(self, request):
        qs = Case.objects.filter(active=True).order_by('-created')[:10]
        context = {
            'items': qs
        }
        return render(request, template_name=self.template_name, context=context)


class CaseDetailView(View):
    template_name = 'cases/detail.html'

    def get(self, request, pk):
        case = get_object_or_404(Case, pk=pk)
        context = {
            'item': case,
        }
        if case.active:
            form = CommentForm()
            context['form'] = form
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, pk):
        form = CommentForm(request.POST)
        case = get_object_or_404(Case, pk=pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.case = case
            if request.POST.get('close-case') == 'close':
                case.active = False
                case.save()
            comment.save()
            return redirect(case.get_absolute_url())
        context = {
            'item': case,
            'form': form
        }
        # return render(request, template_name=self.template_name, context=context)
        return redirect(case.get_absolute_url())


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


class CaseSearchView(View):
    template_name = 'cases/search.html'

    def get(self, request):
        form = SearchForm()
        title = None
        module = None
        active = True
        results = []
        if 'title' or 'module' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                module = form.cleaned_data.get('module')
                active = form.cleaned_data.get('active')
                print(active)
                if title:
                    results.extend(Case.objects.filter(title__icontains=title))
                if module:
                    results.extend(Case.objects.filter(module=module))
        context = {
            'form': form,
            'module': module,
            'title': title,
            'results': results
        }
        return render(request, template_name=self.template_name, context=context)
