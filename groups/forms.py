from django import forms
from django_filters import FilterSet

from groups.models import Group
from students.models import Student


class StudentInGroup(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def save(self, commit=True):
        new_group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()

    class Meta:
        model = Group
        fields = '__all__'
        # [
        #     'group_name',
        #     'start_date',
        #     'group_description',
        #
        #
        # ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})

        }


class CreateGroupForm(StudentInGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group__isnull=True)

    class Meta(StudentInGroup.Meta):
        pass


class UpdateGroupForm(StudentInGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all()

    class Meta(StudentInGroup.Meta):
        pass

    def clean_group_name(self):
        value = self.cleaned_data.get('group_name')
        return value.capitalize()

    def clean_group_description(self):
        value = self.cleaned_data.get('group_description')
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


class FilterGroupForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
            'start_date': ['exact', 'gte', 'lte'],
            'end_date': ['exact', 'gte', 'lte']
        }
