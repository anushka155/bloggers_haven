from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Article, Category, Comment
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'category.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article)

    is_author = False
    if request.user.is_authenticated and article.author:
        try:
            is_author = (request.user.id == article.author.id)
        except AttributeError:
            is_author = (request.user.username == str(article.author))

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
        'is_author': is_author,
    }
    return render(request, 'article.html', context)


def like_article(request, article_id):
    print("LIKE VIEW HIT")
    if not request.user.is_authenticated:
        print("USER NOT AUTHENTICATED")
        return JsonResponse({'error': 'login_required'}, status=403)
    article = Article.objects.get(id=article_id)
    already_liked = article.likes.filter(id=request.user.id).exists()
    print("Already liked before toggle:", already_liked)

    if already_liked:
        article.likes.remove(request.user)
        liked = False
        print("Removed like")
    else:
        article.likes.add(request.user)
        liked = True
        print("Added like")

    print("Total likes now:", article.likes.count())
    return JsonResponse({'liked': liked, 'total_likes': article.likes.count()})


def add_comment(request, article_id):
    content = request.POST.get("content")

    comment = Comment.objects.create(
        article_id=article_id,
        author=request.user,
        content=content,
        created_at=timezone.now()
    )

    return JsonResponse({
        "success": True,
        "author": comment.author.username,
        "content": comment.content,
        "created_date": comment.created_at.strftime("%Y-%m-%d %H:%M")
    })


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                url = request.GET.get('next', '/')
                return redirect(url)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('user_login')


@login_required
def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user != article.author:
        return redirect('article', article_id=article.id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'update_article.html', {'form': form, 'article': article})


@login_required
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.user != article.author:
        return redirect('article', article_id=article.id)

    if request.method == 'POST':
        article.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'article': article})


@login_required
def my_articles(request):
    articles = Article.objects.filter(
        author=request.user).order_by('-published_date')
    return render(request, 'my_articles.html', {'articles': articles})
