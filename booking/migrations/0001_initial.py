# Generated by Django 4.2.1 on 2023-05-09 10:03

import datetime
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
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capsule', models.CharField(max_length=100, verbose_name='Капсула')),
                ('dayIn', models.DateField(default=datetime.datetime.now, verbose_name='Дата заїзду')),
                ('dayOut', models.DateField(default=datetime.datetime.now, verbose_name='Дата виїзду')),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Час замовлення')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Бронювання',
                'verbose_name_plural': 'Бронювання',
            },
        ),
    ]
