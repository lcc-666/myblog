from django.urls import path, include
from blogs.views import *

app_name='[blogs]'
urlpatterns=[
    path('index/',IndexView.as_view(),name='index'),
    path('article/',ArticleView.as_view(),name='article'),
    path('detail/<int:pk>',DetailView.as_view(),name='detail'),
    path('filing/<int:year>/<int:month>',FilingView.as_view(),name='filing')
]