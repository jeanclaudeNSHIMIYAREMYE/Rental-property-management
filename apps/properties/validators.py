from django.core.exceptions import ValidationError


def validate_monthly_rent(value):
    if value <= 0:
        raise ValidationError(
            "Le loyer mensuel doit être supérieur à 0."
        )


def validate_surface_area(value):
    if value <= 0:
        raise ValidationError(
            "La superficie doit être supérieure à 0."
        )
        
def validate_deposit(value):
    if value <=0:
        raise ValidationError("Caution doit être supérieure à 0.")