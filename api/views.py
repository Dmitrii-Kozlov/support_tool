from django.shortcuts import render
from rest_framework import generics
from .serializers import CaseSerializer
from cases.models import Case


class CaseApiView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer