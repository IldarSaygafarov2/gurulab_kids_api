from django.db import models

# Create your models here.


class Stock(models.Model):
    title = models.CharField(verbose_name="Название акции", max_length=100)
    descr = models.CharField(verbose_name="Описание акции", max_length=100)

    def __str__(self):
        return self.title
