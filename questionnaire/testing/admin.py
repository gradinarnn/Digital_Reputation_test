from django import forms
from django.contrib import admin

# Register your models here.
from django.forms import formset_factory, inlineformset_factory

from testing.models import Test, Question, Answer

# admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
#



class ItemInline(admin.StackedInline):
    model = Question
    extra = 1

    filter_horizontal = ['answers', 'correct_answers']


class TestAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Test, TestAdmin)