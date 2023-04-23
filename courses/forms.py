from django import forms
from django_filters import FilterSet

from courses.models import Course


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})

        }


class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})

        }

    def clean_course_name(self):
        value = self.cleaned_data.get('course_name')
        return value.capitalize()

    def clean_course_description(self):
        value = self.cleaned_data.get('course_description')
        sentences = value.split('.')
        final_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            sentence = sentence.capitalize()
            final_sentences.append(sentence)
        final_text = '. '.join(final_sentences)
        final_text = final_text + '.'
        return final_text


class FilterCourseForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact', 'icontains'],
            'start_date': ['exact', 'gte', 'lte']
        }
