# Generated by Django 4.0.3 on 2022-03-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]