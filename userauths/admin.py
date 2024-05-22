from django.contrib import admin
from userauths.models import User, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'date']
    

admin.site.register(User)

# Register your models here.
