from django.test import SimpleTestCase
from model_bakery import baker
from person.models import Person


class PersonTestCase(SimpleTestCase):
    def setUp(self):
        self.person = baker.prepare(Person)

    def test_return_method_get_full_name(self):
        full_name = f'{self.person.first_name.title()} {self.person.last_name.title()}'.strip()

        self.assertEqual(full_name, self.person.get_full_name())

    def test_return_str(self):
        self.assertEqual(str(self.person), self.person.get_full_name())
