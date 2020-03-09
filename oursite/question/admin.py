from django.contrib import admin

# Register your models here.
from .models import Question, OriginInfo

admin.site.register(Question)
admin.site.register(OriginInfo)