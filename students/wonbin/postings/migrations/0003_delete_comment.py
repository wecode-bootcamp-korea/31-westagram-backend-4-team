# Generated by Django 4.0.3 on 2022-03-24 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_timezone_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
