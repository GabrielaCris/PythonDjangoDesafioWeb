# Generated by Django 4.0.5 on 2022-06-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('N_de_vendas', models.CharField(max_length=100)),
                ('Nf', models.CharField(max_length=100)),
                ('Serviços_executados', models.CharField(max_length=100)),
            ],
        ),
    ]
