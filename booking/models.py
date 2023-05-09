from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='User')
    capsule = models.CharField(max_length=100, verbose_name='Капсула')
    dayIn = models.DateField(default=datetime.now, verbose_name='Дата заїзду')
    dayOut = models.DateField(default=datetime.now, verbose_name='Дата виїзду')
    time_ordered = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Час замовлення')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Ціна')
    def __str__(self):
        return f"{self.user.username} | dayIn: {self.dayIn} | dayOut: {self.dayOut}"
    
    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'

