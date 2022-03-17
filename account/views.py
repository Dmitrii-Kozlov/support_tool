from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .forms import LoginForm
# Create your views here.


class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd.get('username'), password=cd.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Successful')
                else:
                    return HttpResponse('disabled')
            else:
                return HttpResponse('Invalid login')