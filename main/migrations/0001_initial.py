# Generated by Django 4.2.5 on 2023-09-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=300)),
                ('result', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
