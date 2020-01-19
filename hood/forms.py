from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['username', 'description', 'name', 'email']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['username','neighbourhood','profpic']
    

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['owner','neighbourhood','description']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields = ['logo', 'neighbourhood', 'name', 'email', 'contact', 'address']
        
class AuthorityForm(forms.ModelForm):
    class Meta:
        model= Authorities
        fields = ['neighbourhood', 'name', 'email', 'contact', 'description']
 
