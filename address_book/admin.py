from django.contrib import admin
from .models import addressModel
class AdminAddress(admin.ModelAdmin):
    list_display = ['Name','Email','Mobile','City']
# Register your models here.
admin.site.register(addressModel,AdminAddress)