from django import forms
from .models import MyModel
from django.core import validators

def age_chk(value):
    if value == 18:
        raise forms.ValidationError('Error')
    return value


def age_chk2(value):
    if value == 19:
        raise forms.ValidationError('Error2')
    return value


## --------------- Simple Form -------------- ##
class MyForm(forms.Form):
    first = forms.CharField(label='First', label_suffix=' :-', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-1'}), validators=[validators.MinLengthValidator(5)])
    last = forms.CharField(label='Last', label_suffix=' :-', min_length=5, widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))
    age = forms.IntegerField(label='Age', label_suffix=' :-', widget=forms.NumberInput(attrs={'class': 'form-control mb-1'}), validators=[age_chk,age_chk2])


    ### ------------ Single Field Data Vadidator/ Cleaner for Data Checking Manual -----------
    # def clean_age(self):
    #     data = self.cleaned_data["age"]
    #     if data <= 18:
    #         raise forms.ValidationError('Age Not Less Than 18')
    #     return data



    ### ------------ Multi Field Data Vadidator/ Cleaner for Data Checking Manual -----------
    # def clean(self):
    #         cleaned_data = super().clean()
    #         first = self.cleaned_data['first']
    #         if first == 'Naresh':
    #             raise forms.ValidationError('This First Name Not is Accept', first)
    #         last = self.cleaned_data['last']
    #         if last == 'Kumar':
    #             raise forms.ValidationError('This last Name Not is Accept', last)
    #         age = self.cleaned_data['age']
    #         if age <= 18:
    #             raise forms.ValidationError('This Age is Not Accept', age)
                
    


## --------------- Manual Model Form -------------- ##
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['first', 'last', 'age']
        widgets = {
            'first' : forms.TextInput(attrs={'class' : 'form-control mb-1'}),
            'last' : forms.TextInput(attrs={'class' : 'form-control mb-1'}),
            'age' : forms.NumberInput(attrs={'class' : 'form-control mb-1'}),
        } 

        
    