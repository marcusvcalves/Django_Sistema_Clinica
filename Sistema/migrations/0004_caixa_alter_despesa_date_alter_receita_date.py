# Generated by Django 4.1.6 on 2023-02-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0003_despesa_receita_alter_paciente_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=3, max_digits=12)),
            ],
        ),
        migrations.AlterField(
            model_name='despesa',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='receita',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
