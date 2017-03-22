from django.contrib import admin

# Register your models here.
from .models import SectionItem
from .models import Fruit

admin.site.register(SectionItem)
admin.site.register(Fruit)