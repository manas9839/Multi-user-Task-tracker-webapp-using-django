from django import forms
from django.forms import ModelForm
from tasks.models import Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        widgets = {
            'due_date': DateInput(),
        }
        fields = ['title', 'due_date',]

class UpdateForm(forms.Form):
    nt = forms.CharField(max_length=150, label="New Title", widget=forms.Textarea(attrs={'rows':3, 'cols':30}))
    nd = forms.DateField(widget=DateInput)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, label="First name",required=True)
    last_name = forms.CharField(max_length=50, label="Last name",required=True)

    class Meta:
    	model = User
    	fields = ("username","first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
        	user.save()
        return user

class ProfileUpdateForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, label="First name",required=True)
    last_name = forms.CharField(max_length=50, label="Last name",required=True)
    user = forms.CharField(max_length=150,label="Username", required=True)