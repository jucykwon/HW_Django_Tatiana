from django import forms
from django_filters import FilterSet, filters
from django.db.models import Q
from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'city',
            'birthday',

        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})

        }


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'phone',
            'city',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})

        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        return value.capitalize()

    def clean_phone(self):
        student_phone = self.cleaned_data.get('phone')
        student_phone = ''.join(filter(lambda x: x.isdigit() or x in ['-', '+', '(', ')'], student_phone))
        if len(student_phone) == 10:
            student_phone = '+38' + student_phone
        elif len(student_phone) == 12 and student_phone.startswith('38'):
            student_phone = '+' + student_phone
        elif len(student_phone) == 13 and student_phone.startswith('+38'):
            pass
        else:
            raise forms.ValidationError("Invalid phone number")
        return student_phone


class FilterStudentForm(FilterSet):

    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
