from django.core.exceptions import ValidationError

def name_validator(value):
    if len(value) < 3:
        raise ValidationError(
            ('Name\'s must be at least 3 charachters long'),
            params={'value': value},
        )