

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Bus,Book



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegFrom(UserCreationForm):
    Mobile=forms.CharField(max_length=15,required=True)
    # image=forms.FileField(required=True,max_length=500)
    Address=forms.CharField(max_length=100,required=True)
    place=forms.CharField(max_length=30)
    birth_date = forms.DateField(label="DATE OF BIRTH", widget=forms.DateInput(attrs={'type': 'date'}),)
    class Meta:
        model =User
        fields =['username','first_name' ,'last_name','birth_date','Address','place','Mobile','email' ,'password1' ,'password2']

class FindbusForm(ModelForm) :
    source=forms.CharField(max_length=10,label='Source')
    dest=forms.CharField(max_length=10,label='Destination')
    date=forms.DateField(label='Date of Journey',widget=forms.DateInput(attrs={'type':'date'}),)
    class Meta:
        model=Bus
        fields={'source','dest','date'}
class BookForm(ModelForm):
    nos=forms.CharField(required=True,label='Number of Seat')
    id=forms.CharField(required=True,label='BUS ID')

    class Meta:
        model=Bus
        fields={'id','nos'}

#add bus
class Addbus(ModelForm):
    bus_name=forms.CharField(max_length=100,required=True,label='Name')
    source=forms.CharField(max_length=50,required=True,label='Source')
    dest=forms.CharField(max_length=20,required=True,label='Destination')
    nos=forms.IntegerField(required=True,label="Number of seat")
    rem=forms.IntegerField(required=True,label="Remaining seat")
    price=forms.DecimalField(required=True)
    date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    time=forms.TimeField(widget=forms.TimeInput)
    class Meta:
        model=Bus
        fields=['bus_name','source','dest','nos','rem','price','date','time']
class datesearchForm(ModelForm):
    date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model=Book
        fields={'date'}