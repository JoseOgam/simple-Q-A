from django.contrib import admin

# making poll app modifiable in admin interface.

from django.contrib import admin
from django.utils import timezone
from django.utils.datetime_safe import datetime

from .models import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


list_display = ('question_text', 'pub_date', 'was_published_recently')


def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now


was_published_recently.admin_order_field = 'pub_date'
was_published_recently.boolean = True
was_published_recently.short_description = 'Published recently?'

list_filter = ['pub_date']
