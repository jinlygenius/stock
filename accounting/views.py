from django.db import transaction
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import *
from .serializers import *


class RecordListCreateView(generics.ListCreateAPIView):
    '''
    '''
    serializer_class = RecordSerializer
    queryset = Record.objects.all()

    # def get_queryset(self):
    #     return Record.objects.all()


class RecordRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    '''
    '''
    serializer_class = RecordSerializer
    queryset = Record.objects.all()