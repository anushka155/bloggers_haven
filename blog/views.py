from django.shortcuts import render, redirect
from .models import Article, Category, Comment
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'login_required'}, status=403)
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
    return JsonResponse({'success': True})

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