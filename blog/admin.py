from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Student)
admin.site.register(models.Book)
admin.site.register(models.Course)

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 0

class QuestionAdmin (admin.ModelAdmin):
    
    list_display = ( 'question_text' , 'publish_date' , 'was_published_recently' ) # 필드 출력
    list_filter = ['publish_date'] # 검색 필터
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['publish_date']}),] # 상세 보기 화면
    inlines = [ChoiceInline] # inline 추가
        
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)