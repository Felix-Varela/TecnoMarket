# Generated by Django 3.2.6 on 2021-08-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='images',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
