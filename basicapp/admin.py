from django.contrib import admin

# Register your models here.
from .models import Sendmessage

class Sendmess(admin.ModelAdmin):
    pass
admin.site.register(Sendmessage,Sendmess)
