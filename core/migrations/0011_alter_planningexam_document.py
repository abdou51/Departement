# Generated by Django 4.1.6 on 2023-02-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_planningexam_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planningexam',
            name='document',
            field=models.ImageField(upload_to='images'),
        ),
    ]
