# Generated by Django 4.2.3 on 2023-07-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('contacts', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
