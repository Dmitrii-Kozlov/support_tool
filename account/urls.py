from django.contrib.auth.views import (LogoutView,
                                       LoginView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       )
from django.urls import path
from .views import EditView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('edit/', EditView.as_view(), name='edit')
]