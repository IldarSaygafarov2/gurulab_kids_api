from django.urls import path
from . import views

urlpatterns = [
    path("stocks/", views.StockList.as_view()),
    path("courses/", views.CourseList.as_view()),
    path("add_item/", views.post_test_data)
]
