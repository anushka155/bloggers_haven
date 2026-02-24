from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('article/<int:article_id>/', article, name='article'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('article/<int:article_id>/comment/', add_comment, name='add_comment'),
    path('write/', create_article, name='create_article'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('article/<int:article_id>/delete/', delete_article, name='delete_article'),
    path('article/<int:article_id>/update/', update_article, name='update_article'),
    path('tinymce/', include('tinymce.urls')),
    path('my-articles/', my_articles, name='my_articles'),
]
