from django.contrib import admin
from .models import Type, Question, Patient, Response, Question_Response

# Register your models here.

admin.site.register(Type)
admin.site.register(Question)
admin.site.register(Patient)
admin.site.register(Response)
admin.site.register(Question_Response)