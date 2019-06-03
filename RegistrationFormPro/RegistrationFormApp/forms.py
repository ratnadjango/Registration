from django import forms

class RegistrationForm(forms.Form):

    first_name = forms.CharField(
        label="First_name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '1st name'
            }
        )
    )
    last_name = forms.CharField(
        label="Last_name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'last_name'
            }
        )
    )
    email_id = forms.EmailField(
        label="Email id",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Id'
            }
        )
    )
    mobile_number = forms.IntegerField(
        label="Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile num'
            }
        )
    )
    user_name = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )
    password = forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'enter your password'
            }
        )
    )
    password1 = forms.CharField(
        label="enter your paasowd",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'conformation password'
            }
        )
    )

class LoginForm(forms.Form):

    user_name = forms.CharField(
        label="enter your user name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your username'
            }
        )
    )
    password = forms.CharField(
        label="enter ur password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )