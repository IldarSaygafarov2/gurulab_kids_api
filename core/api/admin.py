from django.contrib import admin
from .models import Stock, Course, CourseItem

# Register your models here.


class CourseItemInline(admin.TabularInline):
    model = CourseItem
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [
        CourseItemInline
    ]


admin.site.register(Stock)
admin.site.register(Course, CourseAdmin)