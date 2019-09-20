from django import forms
from django.forms import (CharField, DateTimeField, ModelChoiceField,
                          ModelForm, ModelMultipleChoiceField)
from django.contrib.auth.models import User
from .models import Piece


class ArticleForm(ModelForm):
    class Meta:
        model = Piece
        fields = ['subject', 'description', 'piece_type']