from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .forms import CaseForm, CommentForm, SearchForm
from .models import Case


class CaseListView(LoginRequiredMixin, View):
    template_name = 'cases/list.html'

    def get(self, request):
        qs = Case.objects.filter(active=True).order_by('-created')[:10]
        context = {
            'items': qs
        }
        return render(request, template_name=self.template_name, context=context)


class CaseDetailView(LoginRequiredMixin, View):
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
        form = CommentForm(request.POST, request.FILES)
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


class CaseCreateView(LoginRequiredMixin, View):
    template_name = 'cases/create.html'

    def get(self, request):
        form = CaseForm()
        context = {
            'form': form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            case = form.save(commit=False)
            case.author = request.user
            # case.docfile = request.FILES['docfile']
            case.save()
            return redirect(case.get_absolute_url())
        context = {
            'form': form
        }
        return render(request, template_name=self.template_name, context=context)


class CaseSearchView(LoginRequiredMixin, View):
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
                if title and module:
                    qs = Case.objects.filter(title__icontains=title).filter(module=module)
                    if active:
                        qs.filter(active=active)
                    results.extend(qs)
                elif title:
                    qs = Case.objects.filter(title__icontains=title)
                    if active:
                        qs.filter(active=active)
                    results.extend(qs)
                elif module:
                    qs = Case.objects.filter(module=module)
                    if active:
                        qs.filter(active=active)
                    results.extend(qs)
        context = {
            'form': form,
            'module': module,
            'title': title,
            'results': results
        }
        return render(request, template_name=self.template_name, context=context)
