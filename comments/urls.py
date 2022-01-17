from django.urls import path

from comments.views import CreateVIem

app_name = '[comments]'
urlpatterns = [
    path('create/<int:pk>', CreateVIem.as_view(), name='create')
]
