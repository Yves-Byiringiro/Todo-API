from django.contrib import admin
from .models import Todo




class TodoAdmin(admin.ModelAdmin):
    list_display = ['title','description','priority','createDate','modifiedDate']
    list_filter = ['priority','createDate']
    list_per_page = 10


admin.site.register(Todo,TodoAdmin)
