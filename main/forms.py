from django import forms

from .models import Post, UserResponse


class NewPostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
            'upload',
        ]


class ResponseCreate(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = [
            'text',
        ]
