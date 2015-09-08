from django.contrib import admin

from .models import Content, Question

#  this class builds a friendly admin interface


class QuestionAdmin(admin.TabularInline):
    model = Question

#  This class adds the Question Model to the Content Model for easier data input


class ContentAdmin(admin.ModelAdmin):
    inlines = [
        QuestionAdmin,
    ]
#  This line registers the classes with the Admin


admin.site.register(Content, ContentAdmin)
