from django.shortcuts import render, redirect
from .models import Article, Category, Comment
from .forms import CommentForm

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

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article', article_id=article.id)
    context = {
        'article': article,
        'comments': comments,
        'form': form,
        'total_likes': article.likes.count(),
        'liked': article.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
    }
    return render(request, 'article.html', context)

def like_article(request, article_id):
    if not request.user.is_authenticated:
        return redirect('login')
    article = Article.objects.get(id=article_id)
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
    return redirect('article', article_id=article.id)


