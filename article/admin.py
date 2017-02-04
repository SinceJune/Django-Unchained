from django.contrib import admin
from article.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time')


admin.site.register(Article, ArticleAdmin)
