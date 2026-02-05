from django.shortcuts import render, redirect
from .models import Article, Category, Comment

# Create your views here.
def home(request):
    context = {
        'articles': Article.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'index.html', context)

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category=category)
    context = {
        'category': category,
        'articles': articles,
    }
    return render(request, 'category.html', context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article)
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'article.html', context)


