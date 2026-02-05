from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('article/<int:article_id>/', article, name='article'),
]
