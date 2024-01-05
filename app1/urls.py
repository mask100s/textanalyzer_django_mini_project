from django.urls import path
from app1.views import * 

app_name='connect_1'

urlpatterns = [
    path('home/', home, name="home"),
    path('analyzingtext/', analyzingtext, name="analyzingtext"),
    path('analyzedtext/', analyzedtext, name="analyzedtext"),
]
