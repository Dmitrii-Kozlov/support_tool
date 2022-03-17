from django.contrib.auth.views import (LogoutView,
                                       LoginView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       )
from django.urls import path, reverse_lazy
from .views import EditView, ArchiveView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('edit/', EditView.as_view(), name='edit'),
    path('archive/', ArchiveView.as_view(), name='archive'),
]