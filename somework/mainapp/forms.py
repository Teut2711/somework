from django import forms
# Create your forms here.

class UploadFileForm(forms.Form):
    host = forms.CharField()
    emailaddress = forms.EmailField(label="Enter Email ",required=True)
    password = forms.CharField(label="Enter Password " , widget=forms.PasswordInput, required=True, min_length=8)
    filepath = forms.FileField(label="Select File ",required=True)
    