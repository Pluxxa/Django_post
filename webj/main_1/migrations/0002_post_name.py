# Generated by Django 5.0.7 on 2024-07-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='default_name', max_length=20, verbose_name='Имя'),
        ),
    ]
