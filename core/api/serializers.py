from rest_framework import serializers
from .models import Stock, Course, CourseItem, TestModel


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["id", "title", "descr"]


class CourseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseItem
        fields = ["id", "title", "content"]


class CourseSerializer(serializers.ModelSerializer):
    course_items = CourseItemSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "title", "sub_title", "course_items"] 
    

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ["id", "title", "content"]
