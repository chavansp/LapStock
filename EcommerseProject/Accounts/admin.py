from django.contrib import admin

# Register your models here.
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ['mobile_no','email']

admin.site.register(CustomUser,UserAdmin)