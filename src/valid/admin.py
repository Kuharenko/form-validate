from django.contrib import admin
from valid.models import Car
# Register your models here.

admin.autodiscover()

admin.site.register(Car)