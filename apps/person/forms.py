from django import forms

from .models import Person


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonRegisterForm(forms.ModelForm):
    birthday = forms.DateField(widget=DateInput(), label='Data de nascimento')

    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'age',
            'birthday',
            'email',
            'nickname',
            'note',
        ]
