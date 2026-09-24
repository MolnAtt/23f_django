from django.contrib import admin

from .models import *
# "from ... import * --- and everything burns "

# Register your models here.

admin.site.register(Darab)
admin.site.register(Mufajka)

