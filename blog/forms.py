from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'What are your thoughts on this article?',
                'rows': 4
            }),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','category','content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title-input',
                'placeholder': 'Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'content-textarea',
                'placeholder': 'Tell your story...',
                'rows': 15
            }),
                'category': forms.Select(attrs={
                    'class': 'category-select',
                }),
                'image': forms.ClearableFileInput(attrs={
                    'class': 'image-input',
                }),
        }