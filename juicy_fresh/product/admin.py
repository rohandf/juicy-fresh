from django.contrib import admin
from .models import fruits
from .models import comment

# Register your models here.

admin.site.register(fruits)
admin.site.register(comment)