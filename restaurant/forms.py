from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from restaurant.models import Cook


def check_years_of_experience(years_of_experience: int) -> int:
    if years_of_experience > 15:
        raise ValidationError(
            "You are a real pro. We cannot afford you."
        )
    return years_of_experience


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "first_name", "last_name",)

    def clean_years_of_experience(self):
        return check_years_of_experience(self.cleaned_data["years_of_experience"])


class CookExperienceUpdateForm(forms.ModelForm):

    class Meta:
        model = Cook
        fields = ("years_of_experience",)

    def clean_years_of_experience(self):
        return check_years_of_experience(self.cleaned_data["years_of_experience"])
