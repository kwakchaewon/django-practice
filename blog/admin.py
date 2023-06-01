from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Student)
admin.site.register(models.Book)
admin.site.register(models.Course)


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):

#     # 원하는 필드
#     list_display = ['title', 'content']

#     # 링크 설정
#     # list_display_links = ['']

#     # 검색 필드
#     search_fields=['title','content']

#     # 검색 필터
#     # list_filter=['is_staff']
