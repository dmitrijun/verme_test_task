from django.db import models

# Create your models here.


class Tree(models.Model):
    parent = models.ForeignKey('self', models.CASCADE, null=True,
                               verbose_name='Родитель')
    name = models.CharField(max_length=255, verbose_name='Название')
