from django.contrib import admin
#from .models import Question , Choice
# Register your models here.
"""from .models import Question , Choice
admin.site.register(Question)
admin.site.register(Choice)"""


#customize admin panel

"""class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_test"]
admin.site.register(Question, QuestionAdmin)
    


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)"""