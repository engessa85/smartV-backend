# Generated by Django 5.1.6 on 2025-03-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_created_at_company_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contract',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
