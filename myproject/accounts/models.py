from django.db import models


# Create your models here.

class Users(models.Model):
    """Модель с юзерами"""

    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    passport_number = models.CharField(max_length=20, unique=True, blank=True, null=True)  # Уникальные данные паспорта
    birth_place = models.CharField(max_length=250, blank=True, null=True)  # Место рождения
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)  # Уникальный номер
    mail = models.EmailField(max_length=50, unique=True, blank=True, null=True)  # Уникальный email
    registration_address = models.CharField(max_length=250, blank=True, null=True)
    residence_address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
