from django.contrib import admin
from .models import Password


class PasswordAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated', 'status')
    list_filter = ('status', 'created', 'updated', 'author')
    search_fields = ('title', 'author')
    raw_id_fields = ('author',)
    date_hierarchy = 'updated'
    ordering = ['status', 'updated']

admin.site.register(Password, PasswordAdmin)
