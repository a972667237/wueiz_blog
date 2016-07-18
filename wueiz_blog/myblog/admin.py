from django.contrib import admin
from .models import article,author,tag
# Register your models here.
admin.site.register(article)
admin.site.register(author)
admin.site.register(tag)