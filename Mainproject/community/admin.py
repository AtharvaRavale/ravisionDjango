from django.contrib import admin
from .models import Motive

# Register your models here.


@admin.register(Motive)
class MotiveAdmin(admin.ModelAdmin):
    list_display=('name','motive_type','created_at',)
    list_filter=('motive_type',)
    search_fields=('name',)
