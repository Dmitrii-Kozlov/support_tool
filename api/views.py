from django.shortcuts import render
from rest_framework import generics

from .permissions import IsAuthorOrReadOnly
from .serializers import CaseSerializer
from cases.models import Case


class CaseApiView(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
