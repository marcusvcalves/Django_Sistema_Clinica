# Generated by Django 4.1.6 on 2023-02-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='birthDate',
            field=models.DateField(default=None, null=True),
        ),
    ]