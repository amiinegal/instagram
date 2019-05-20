from .models import Image,Profile
from django import forms
from django.forms import ModelForm, Textarea, IntegerField


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'likes']

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following']


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
