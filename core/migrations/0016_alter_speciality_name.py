# Generated by Django 4.1.6 on 2023-02-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_speciality_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
