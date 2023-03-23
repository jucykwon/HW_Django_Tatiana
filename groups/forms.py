from django import forms

from groups.models import Group
import string


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'start_date',
            'group_description',

        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})

        }


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'start_date',
            'group_description',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})

        }

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
