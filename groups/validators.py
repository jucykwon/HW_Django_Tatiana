from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(start_date):
    today_day = date.today()
    if start_date < today_day:
        raise ValidationError('The start date of the group cannot be in the past')
