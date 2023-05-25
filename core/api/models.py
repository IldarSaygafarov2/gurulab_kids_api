from django.db import models

# Create your models here.


class Stock(models.Model):
    title = models.CharField(verbose_name="Название акции", max_length=100)
    descr = models.CharField(verbose_name="Описание акции", max_length=100)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class CourseItem(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name="course_items")

    def __str__(self):
        return f"{self.course.title}: {self.title}"