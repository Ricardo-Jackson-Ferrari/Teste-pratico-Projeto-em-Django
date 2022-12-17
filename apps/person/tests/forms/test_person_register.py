from django.forms import ValidationError, model_to_dict
from django.test import TestCase
from model_bakery import baker
from person.forms import PersonRegisterForm
from person.models import Person


class PersonRegisterTestCase(TestCase):
    def test_def_clean_data_lower(self):
        person = baker.prepare(Person, _fill_optional=True)
        person_data = model_to_dict(person, exclude=['id'])
        person_data_upper = {
            k: (v.upper() if isinstance(v, str) else v)
            for (k, v) in person_data.items()
        }
        person_data_lower = {
            k: (v.lower() if isinstance(v, str) else v)
            for (k, v) in person_data.items()
        }

        form = PersonRegisterForm(data=person_data_upper)
        form.cleaned_data = {}
        form._clean_fields()

        self.assertDictEqual(person_data_lower, form.clean())

    def test_def_clean_success(self):
        person = baker.prepare(Person, _fill_optional=True)
        person_data = model_to_dict(person, exclude=['id'])

        form = PersonRegisterForm(data=person_data)
        form.cleaned_data = {}
        form._clean_fields()

        self.assertTrue(form.clean())

    def test_def_clean_raise_validation_error_email(self):
        email = 'email_raise_test@email.com'
        baker.make(Person, email=email)
        person_2 = baker.make(Person)

        person_2_data_update = model_to_dict(person_2)
        person_2_data_update['email'] = email

        form = PersonRegisterForm(data=person_2_data_update)
        form.cleaned_data = {}
        form._clean_fields()

        self.assertRaisesMessage(
            ValidationError, 'Email já existe.', form.clean
        )
