# Generated by Django 4.1 on 2023-05-29 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_noticacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticacao',
            name='status',
        ),
    ]
