# Generated by Django 5.1.6 on 2025-03-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_appointment_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
