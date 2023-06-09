# Generated by Django 4.1.6 on 2023-02-10 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_course_description_alter_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanningExams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(upload_to='images/planningexams/')),
                ('Speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.speciality')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.degree')),
            ],
        ),
    ]
