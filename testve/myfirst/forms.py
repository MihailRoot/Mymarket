from email.policy import default
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class SightUp(UserCreationForm):
    first_name = forms.CharField( widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32)
    last_name = forms.CharField( widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}), max_length=32)
    email = forms.EmailField(widget =forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'}), max_length =64)
    username = forms.CharField(widget =forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(widget =forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), label='Password')
    password2 = forms.CharField(widget =forms.PasswordInput(attrs={'class':'form-control','placeholder':'RepeatPassword'}), label='RepeatPassword')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')
class Oplata(forms.Form):
    oplata = forms.CharField(label='Oplata:')
    #user = forms.CharField(label='Username')
class Product(forms.Form):
      product = forms.CharField(max_length=100,min_length=10)
      text = forms.CharField(widget=forms.Textarea)
    # user = forms.CharField(widget=forms.HiddenInput,required = False,)
    # image= forms.ImageField()
      prices = forms.CharField()
      docker_image = forms.CharField()
     # file = forms.FileField()


    #      model = Prices
    #      fields = [
    #      'product',
    #      'text',
    #      #'image',
    #      'prise',
    #  ] 
    #  def __init__(self,user,*args,**kwargs):
    #       super(Product,self).__init__(*args,**kwargs) 
    #       self.fields['useralot'].quertset = User.objects.filter(id = user.id)
