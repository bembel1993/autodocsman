from django import forms

class NameForm(forms.Form):
    # title = forms.CharField(max_length=250, required=True)
    form = forms.FileField(required=False)

class FirstForm(forms.Form):  
    # firstname = forms.CharField(label="Enter first name",max_length=50)  
    # lastname = forms.CharField(label="Enter last name", max_length = 10)  
    # email = forms.EmailField(label="Enter Email")  
    file = forms.FileField()