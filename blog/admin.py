from django.contrib import admin
from .models import Post, Category, Tag  # 현재 경로의 models.py 안에 있는 Post를 가져다 쓰겠음 

# Register your models here.
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('categoryName', )}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tagName', )}

admin.site.register(Tag, TagAdmin)