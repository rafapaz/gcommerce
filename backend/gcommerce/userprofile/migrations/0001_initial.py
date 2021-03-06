# Generated by Django 2.2.6 on 2019-10-31 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('complement', models.CharField(max_length=100, null=True, verbose_name='Complement')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('phone', models.IntegerField(null=True, verbose_name='Phone')),
                ('cpf', models.IntegerField(null=True, verbose_name='CPF')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, null=True, verbose_name='Gender')),
                ('dt_birth', models.DateField(null=True, verbose_name='Birth date')),
                ('address', models.ManyToManyField(blank=True, related_name='addresses', to='userprofile.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
