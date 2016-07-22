from django.contrib import admin
from .models import article,author,tag


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )



admin.site.register(article,ArticleAdmin)
admin.site.register(author)
admin.site.register(tag)