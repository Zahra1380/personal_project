# Generated by Django 4.1.7 on 2023-04-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0008_contact_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_me',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]