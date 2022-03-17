from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .forms import LoginForm, ProfileEditForm, UserEditForm
from .models import Profile


class EditView(LoginRequiredMixin, View):
    template_name = 'account/edit.html'

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self,request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль обновлен')
        else:
            messages.error(request, 'Ошибка обновления профиля')
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, template_name=self.template_name, context=context)
