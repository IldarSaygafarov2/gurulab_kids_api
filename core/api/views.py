from django.shortcuts import render
from .serializers import StockSerializer, CourseSerializer
from rest_framework import generics
from .models import Stock, Course
# Create your views here.


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer