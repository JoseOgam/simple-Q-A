from django.contrib import admin

# making poll app modifiable in admin interface.

from django.contrib import admin

from .models import Question

admin.site.register(Question)