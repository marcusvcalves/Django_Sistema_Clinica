# Generated by Django 4.1.6 on 2023-02-14 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0006_alter_receita_desc_alter_receita_pago_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despesa',
            name='professional',
        ),
    ]
