from django import forms
# Create your forms here.

class UploadFileForm(forms.Form):
    host = forms.CharField()
    emailaddress = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=8)
    filepath = forms.FileField(required=True)
    