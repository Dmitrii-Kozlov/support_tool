from django.urls import path
from .views import CaseApiView

urlpatterns = [
path('', CaseApiView.as_view())
    ]