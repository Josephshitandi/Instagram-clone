from django import forms
from .models import Image
from django_registration.forms import RegistrationForm

# class NewsLetterForm(RegistrationForm):
#     your_name = forms.CharField(label='First Name',max_length=30)
#     email = forms.EmailField(label='Email')
    
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'Author', 'author_profile', 'likes']
        
        
        
        