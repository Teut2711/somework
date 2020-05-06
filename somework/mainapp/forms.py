from django import forms
# Create your forms here.

class EmailForm(forms.Form):
    host = forms.CharField()
    emailaddress = forms.EmailField(label="Enter Email ",required=True, max_length=20)
    password = forms.CharField(label="Enter Password " , widget=forms.PasswordInput, required=True, min_length=8, max_length=20)
    filepath = forms.FileField(label="Select File ",required=True)
    
class MasterForm(forms.Form):
    filepath = forms.FileField(label="Select File ",required=True)
    