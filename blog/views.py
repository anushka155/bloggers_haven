from django.shortcuts import render, redirect
from .models import Article, Category, Comment

# Create your views here.
def home(request):
    context = {
        'articles': Article.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'index.html', context)

