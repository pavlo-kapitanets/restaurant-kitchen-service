from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormTests(TestCase):
    def test_creation_form_with_first_last_name_years_of_experience_is_valid(self):
        form_data = {
            "username": "test",
            "password1": "usertest1234",
            "password2": "usertest1234",
            "first_name": "test name",
            "last_name": "test surname",
            "years_of_experience": 14
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_experience_grater_than_15_is_not_valid(self):
        form_data = {
            "username": "test",
            "password1": "usertest1234",
            "password2": "usertest1234",
            "first_name": "test name",
            "last_name": "test surname",
            "years_of_experience": 22
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
