from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username', 'description', 'name', 'email']
        
class UpdateprofileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username', 'description']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        exclude=['username','neighbourhood','profpic']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
    
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood','description']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields = ['logo', 'neighbourhood', 'name', 'email', 'contact', 'address']
        
class AuthorityForm(forms.ModelForm):
    class Meta:
        model= Authorities
        fields = ['neighbourhood', 'name', 'email', 'contact', 'description']
 

class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']