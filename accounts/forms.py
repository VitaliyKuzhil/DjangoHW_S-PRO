from django import forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True,
                               max_length=50,
                               label="Нік",
                               widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    first_name = forms.CharField(required=True,
                                 max_length=50,
                                 label="Ім'я",
                                 widget=forms.TextInput(attrs={'class': 'form-control'})
                                 )
    last_name = forms.CharField(required=True,
                                max_length=50,
                                label="Фамілія",
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    email = forms.EmailField(required=True,
                             max_length=50,
                             label="Електрона пошта",
                             widget=forms.TextInput(attrs={'class': 'form-control'})
                             )
    password1 = forms.CharField(required=True,
                                label="Пароль",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                )
    password2 = forms.CharField(required=True,
                                label="Повторіть пароль",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginCreateForm(AuthenticationForm):
    username = forms.CharField(label="Нік",
                               widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'})
                               )

    class Meta:
        model = User
        fields = ('username', 'password')
