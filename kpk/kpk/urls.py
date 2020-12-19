
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp



urlpatterns = [
    path('', mainapp.index),
    path('admin/', admin.site.urls)
    path('phones/',)
]
