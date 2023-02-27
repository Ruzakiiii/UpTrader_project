from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categories(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class All_items(models.Model):
    item_name = models.CharField(max_length=50)

    item_des = models.CharField(max_length=150)

    item_cat = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def get_url(self):
        return reverse('items-detail', args=[self.id])

    def __str__(self):
        return self.item_name

