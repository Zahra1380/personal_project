# Generated by Django 4.1.7 on 2023-04-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0009_alter_contact_me_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recieve_massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('massage', models.TextField()),
            ],
        ),
    ]
