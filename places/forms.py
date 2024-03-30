from django import forms
from .models import Comment

class PlaceCommentForm(forms.ModelForm):
    stars_given = forms.IntegerField(max_value=5, min_value=1)
    comment_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4,"cols":20, 'class': 'form-control', 'placeholder': 'Enter your comment here'}),
        max_length=1000,
        min_length=1
    )
    
    class Meta:
        model = Comment
        fields = ("comment_text", "stars_given")
