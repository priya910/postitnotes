# Generated by Django 3.0.5 on 2020-10-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
