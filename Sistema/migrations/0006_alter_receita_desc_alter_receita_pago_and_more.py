# Generated by Django 4.1.6 on 2023-02-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0005_alter_despesa_value_alter_receita_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='desc',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='receita',
            name='pago',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='receita',
            name='professional',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
