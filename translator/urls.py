from django.urls import path
from .views import translate_text,home

urlpatterns = [
    path('translate/', translate_text, name='translate_text'),
    path('', home ,name='home')
]
