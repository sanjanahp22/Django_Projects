from django import forms
from myapp.models import student


# class studentform(forms.Form):
#     name=forms.CharField()
#  
#     email=forms.EmailField()
 


class studentform(forms.ModelForm):
    class Meta:
        model=student 
        fields='__all__'