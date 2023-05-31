from rest_framework import generics
from rest_framework.response import Response

from .models import Stock, Course, TestModel
from .serializers import StockSerializer, CourseSerializer, TestModelSerializer
from rest_framework.decorators import api_view


# Create your views here.


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(["GET"])
def get_test_data(request):
    data = TestModel.objects.all()
    serializer = TestModelSerializer(data, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def post_test_data(request):
    serializer = TestModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

