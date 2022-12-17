from django import forms

from .models import Person


class PersonRegisterForm(forms.ModelForm):
    def clean(self):
        for field, value in self.cleaned_data.items():
            if isinstance(value, str):
                self.cleaned_data[field] = value.lower()

        cleaned_data = super().clean()
        if (
            Person.objects.exclude(pk=self.instance.pk)
            .filter(email=cleaned_data.get('email'))
            .exists()
        ):
            raise forms.ValidationError('Email já existe.')
        return cleaned_data

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
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'}, format='%Y-%m-%d'
            ),
        }
