from django.contrib import admin
from django.urls import path

from app_elso.views import haliho_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('haliho/', haliho_view),
]
