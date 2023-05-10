from django.db import models
from django.urls import reverse

#Create your models here.
class Capsule(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank = True, verbose_name="Опис")
    image = models.ImageField(upload_to='capsules/', blank= True, verbose_name="Фото капсули")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата змінення")

    class Meta:
        verbose_name = 'Капсула'
        verbose_name_plural = 'Капсули'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("capsule_detail", kwargs={"slug": self.slug})
