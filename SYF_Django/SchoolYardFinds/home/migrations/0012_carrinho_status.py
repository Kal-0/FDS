# Generated by Django 4.1 on 2023-05-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_carrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='status',
            field=models.BooleanField(default='True'),
        ),
    ]