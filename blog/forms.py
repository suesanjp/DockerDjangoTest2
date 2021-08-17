from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):

    text = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))

    class Meta:
        model = Blog
        fields = ["text"]
