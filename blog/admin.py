from django.contrib import admin
from blog.models import Post, Category, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    '''文章管理模型类'''
    # 指定每一页显示10条数据
    list_per_page = 10
    list_display = ['title', 'excerpt', 'created_time', 'category', 'author']
    # 列表上面的搜索框
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)