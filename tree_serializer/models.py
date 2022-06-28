from django.db import models

# Create your models here.


class Tree(models.Model):
    parent = models.ForeignKey('self', models.CASCADE, null=True, blank=True,
                               verbose_name='Родитель')
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self) -> str:
        return f"{self.pk} - {self.name} - {self.parent_pk}"

    @property
    def parent_pk(self):
        if self.parent:
            return self.parent.pk
        
        return None