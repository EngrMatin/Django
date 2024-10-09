from django import forms
from django.core import validators

class Reviewer(forms.Form):
    name = forms.CharField(min_length=3, max_length=30)
    mobile = forms.CharField(label='Mobile Number')
    email = forms.EmailField()
    # compani_email = forms.EmailField(initial='matin@gmail.com', label_suffix=' = ', disabled=True)
    # user_name = forms.CharField(help_text='Use letters and underscore only')
    password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    review = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':31}) )
    # checkbox = forms.CharField(widget=forms.CheckboxInput)
    age = forms.IntegerField(min_value=16, max_value=22)
    cgpa = forms.DecimalField(label='CGPA', min_value=0, max_value=4, max_digits=3, decimal_places=2)
    youtube = forms.BooleanField(label='Have you subscribed the youtube channel?')
    
    # radio = forms.CharField(widget=forms.RadioSelect)
    # files = forms.CharField(widget=forms.FileInput)
    
    def clean(self):
        cleaned_data = super().clean()
        pw = self.cleaned_data['password']
        con_pw = self.cleaned_data['confirm_password']
        
        if pw != con_pw:
            raise forms.ValidationError('Passwords do not match!')
    
    
    
# def clesn_password(self):
#     password_validation = self.cleaned_data['passwoed']
#     if len(password_validation)<8:
#         raise forms.ValidationError('Password should contain at least 8 characters')
#     return password_validation