from django import forms
from django.forms import ModelForm
from .models import Review

class ReviewForm(forms.ModelForm):

    review_title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Add some text here...', 'name': 'something', 'type': 'text'}), label="", required="")
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Add some text here...', 'name': 'content', 'type': 'text'}), label="", required="")
    
    class Meta:
        model = Review
        fields = ['review_title', 'content']