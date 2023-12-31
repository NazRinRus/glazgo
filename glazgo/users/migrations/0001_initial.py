# Generated by Django 4.2.7 on 2023-11-23 14:47

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('role', models.IntegerField(choices=[(0, 'Администратор'), (1, 'Рекрутер'), (2, 'Рекрутер-администратор'), (3, 'Заказчик'), (4, 'Заказчик-администратор')], default=1, verbose_name='Права')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная Почта')),
                ('birthday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('bio', models.CharField(max_length=255, null=True, verbose_name='Биография')),
                ('cover_photo', models.ImageField(null=True, upload_to='covers/')),
                ('company_name', models.CharField(max_length=30, null=True, verbose_name='Название организации')),
                ('description', models.TextField(null=True, verbose_name='Описание организации')),
                ('legal_address', models.CharField(max_length=250, null=True, verbose_name='Юридический адрес')),
                ('mailing_address', models.CharField(max_length=250, null=True, verbose_name='Почтовый адрес')),
                ('inn', models.CharField(max_length=10, null=True, verbose_name='ИНН')),
                ('checking_account', models.CharField(max_length=20, null=True, verbose_name='Расчетный счет')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
