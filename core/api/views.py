from django.shortcuts import render
from .serializers import StockSerializer
from rest_framework import generics
from .models import Stock
# Create your views here.


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    