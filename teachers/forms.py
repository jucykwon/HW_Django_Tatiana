from django import forms
from django_filters import FilterSet

from teachers.models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'salary',

        ]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})

        }


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'salary',
        ]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})

        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        return value.capitalize()


class FilterTeacherForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
