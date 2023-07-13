from django.core.validators import ValidationError

def validate_start_date_less_than_end_date(value):
    start_date = value.get('start_date')
    end_date = value.get('end_date')

    if start_date > end_date:
        raise ValidationError("Start date must be less than end date")

