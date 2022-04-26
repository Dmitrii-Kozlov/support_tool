from django.urls import path
from .views import CaseApiView, CaseDetailApiView

urlpatterns = [
        path('', CaseApiView.as_view()),
        path('<int:pk>/', CaseDetailApiView.as_view())
    ]