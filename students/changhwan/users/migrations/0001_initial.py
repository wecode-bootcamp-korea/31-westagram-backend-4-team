# Generated by Django 4.0.3 on 2022-03-17 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'names',
            },
        ),
    ]
