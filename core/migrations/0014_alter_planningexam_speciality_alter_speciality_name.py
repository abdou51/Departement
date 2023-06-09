# Generated by Django 4.1.6 on 2023-02-12 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_degree_name_alter_planningexam_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planningexam',
            name='Speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.speciality'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
