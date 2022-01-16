from django.urls import path, include
from blogs.views import *

app_name='[blogs]'
urlpatterns=[
    path('index/',IndexView.as_view())
]