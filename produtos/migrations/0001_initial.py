# Generated by Django 4.0.5 on 2022-06-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('código', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
                ('preço', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
            ],
        ),
    ]
