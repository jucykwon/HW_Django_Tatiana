import sqlite3

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

DOMAINS = ('gmail.com', 'yahoo.com', 'hotmail.com')


def validate_email_domain(value):
    # domains = ('gmail.com', 'yahoo.com', 'hotmail.com')
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError(f'Emails domain "{domain}" is not correct.')


@deconstructible
class ValidateEmailDomains:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f'Emails domain "{domain}" is invalid.')

# def validate_unique_email(value):
#    student_email = value
#    if student_email in student_email:
#        raise ValidationError(f'User with "{student_emails}" already exists.')

# def validate_unique_email(self):
#    email = self.cleaned_data.get["email"]
#    if not User.objects.filter(email=email).exists():
#        raise ValidationError(f'User with "{email}" already exists.')

def validate_unique_email(email):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE email=?", (email,))
    result = cursor.fetchone()
    if result:
        raise ValidationError(f'User with email: "{email}" already exists.')
    else:
        return True
