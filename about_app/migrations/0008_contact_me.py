# Generated by Django 4.1.7 on 2023-04-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0007_alter_education_site_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('telegram', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=50)),
            ],
        ),
    ]
