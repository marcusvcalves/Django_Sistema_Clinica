# Generated by Django 4.1.7 on 2023-04-01 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dentista',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Sistema.dentista'),
            preserve_default=False,
        ),
    ]
