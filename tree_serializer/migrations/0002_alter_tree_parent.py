# Generated by Django 4.0.5 on 2022-06-28 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_serializer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_serializer.tree', verbose_name='Родитель'),
        ),
    ]
