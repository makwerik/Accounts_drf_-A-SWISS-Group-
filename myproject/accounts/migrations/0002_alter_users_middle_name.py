# Generated by Django 5.1 on 2024-08-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
