from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('article/<int:article_id>/', article, name='article'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('article/<int:article_id>/comment/', add_comment, name='add_comment'),
]
