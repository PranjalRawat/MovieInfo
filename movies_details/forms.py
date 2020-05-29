from django import forms

from .models import AddProduct, User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields=[
            "category",
            "movie_name",
            "description",
            "image",
            "director",
            "actors",
            "release_date",
            "language",
            "genre",
            "country",
        ]
        widgets = {
            "release_date": DateInput(),
        }

    def clean_user(self, *args, **kwargs):
        user = self.changed_data.get("User")
        if user == "abc":
            raise forms.ValidationError("Cant be ABC")
        return user


class UserCreateForm(UserCreationForm):

    class Meta:
        fields =('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        