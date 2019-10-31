from django.db import models
from django.contrib.auth import get_user_model


class Address(models.Model):
    street = models.CharField('Street', max_length=100, null=False)
    complement = models.CharField('Complement', max_length=100, null=True)
    city = models.CharField('City', max_length=100, null=False)
    state = models.CharField('State', max_length=100, null=False)
    country = models.CharField('Country', max_length=100, null=False)

    def __str__(self):
        return '{} {} / {} - {} - {}'.format(str(self.street), str(self.complement), str(self.city), str(self.state), str(self.country))

class UserProfile(models.Model):
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female')
        )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100, null=False)
    email = models.EmailField('Email', max_length=100, unique=True)
    phone = models.IntegerField('Phone', null=True)
    cpf = models.IntegerField('CPF', null=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default='M', null=True)
    dt_birth = models.DateField('Birth date', null=True)
    address = models.ManyToManyField(Address, related_name='addresses', blank=True)

    def __str__(self):
        return self.name

