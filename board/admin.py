from django.contrib import admin
from .models import Post, Category, Comment
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
