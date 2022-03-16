from django.urls import path
from .views import CaseListView, CaseDetailView, CaseCreateView, CaseSearchView

app_name = 'cases'

urlpatterns = [
    path('', CaseListView.as_view(), name='list'),
    path('<int:pk>/', CaseDetailView.as_view(), name='detail'),
    path('create/', CaseCreateView.as_view(), name='create'),
    path('search/', CaseSearchView.as_view(), name='search')
]