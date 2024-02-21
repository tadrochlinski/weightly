from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')],
                              widget=forms.Select(attrs={'class': 'form-control'}))
    
    height = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    age = forms.IntegerField(min_value=15, max_value=100, 
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    lifestyle_choices = [
        ('sedentary', 'Sedentary'),
        ('low_activity', 'Low Activity'),
        ('moderate_activity', 'Moderate Activity'),
        ('active', 'Active'),
        ('athlete', 'Athlete'),
    ]
    
    lifestyle = forms.ChoiceField(choices=lifestyle_choices,
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    goal_choices = [
        ('lose_weight', 'Lose Weight'),
        ('maintain_weight', 'Maintain Current Weight'),
        ('gain_weight', 'Gain Weight'),
    ]

    goal = forms.ChoiceField(choices=goal_choices,
                             widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',
                  'gender', 'height', 'age', 'lifestyle', 'goal')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile

class UserProfileForm(UserChangeForm):
    height = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    age = forms.IntegerField(min_value=15, max_value=100, 
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    lifestyle_choices = [
        ('sedentary', 'Sedentary'),
        ('low_activity', 'Low Activity'),
        ('moderate_activity', 'Moderate Activity'),
        ('active', 'Active'),
        ('athlete', 'Athlete'),
    ]
    
    lifestyle = forms.ChoiceField(choices=lifestyle_choices,
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    goal_choices = [
        ('lose_weight', 'Lose Weight'),
        ('maintain_weight', 'Maintain Current Weight'),
        ('gain_weight', 'Gain Weight'),
    ]

    goal = forms.ChoiceField(choices=goal_choices,
                             widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('height', 'age', 'lifestyle', 'goal')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields.pop('password', None)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
    def save(self, commit=True):
        user_profile = super().save(commit=False)
        
        if commit:
            user_profile.save()

        return user_profile