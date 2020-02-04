from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(Page):
    list_display = ('title', 'category', 'URL')


# Register your models here.
admin.site.register(Category)
admin.site.register(Page)

