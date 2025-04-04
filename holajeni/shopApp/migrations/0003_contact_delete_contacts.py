# Generated by Django 5.1.6 on 2025-03-14 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
