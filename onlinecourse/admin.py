from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner,Question,Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 5
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 4

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]
    list_display = ['title']


# <HINT> Register Question and Choice models here

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display=['question_text']
    

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
