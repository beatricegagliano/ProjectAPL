from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Choice, Utente
from .models import Question

admin.site.register(Question)

admin.site.register(Choice)
admin.site.register(Utente)