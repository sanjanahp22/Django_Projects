from django import forms
from myapp.models import student


# class studentform(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     place=forms.CharField()
#     email=forms.EmailField()
#     dob=forms.DateField() 
#     feedback=forms.CharField(widget=forms.Textarea)   


class studentform(forms.ModelForm):
    class Meta:
        model=student 
        fields='__all__'
        
    
    