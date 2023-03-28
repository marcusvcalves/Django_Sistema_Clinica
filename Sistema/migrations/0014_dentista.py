# Generated by Django 4.1.6 on 2023-03-25 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0013_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('cpf', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('cep', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True)),
            ],
        ),
    ]