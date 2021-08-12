from django.contrib import admin
from .models import Post

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['e_name', 'e_salary', 'e_addrs']

admin.site.register(Post, EmployeeAdmin)