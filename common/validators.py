from rest_framework.exceptions import ValidationError
from datetime import date, datetime

def validate_user_age(birthdate_str):
    if not birthdate_str:
        raise ValidationError("Дата рождения не указана в профиле.")
    
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    today = date.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )
    
    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")