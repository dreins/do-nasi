# Generated by Django 4.1 on 2022-10-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_overview', '0006_donasi_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='donasi',
            name='Donation',
            field=models.BooleanField(default=False),
        ),
    ]