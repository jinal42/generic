# Generated by Django 4.0.5 on 2022-06-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('num', models.IntegerField(blank=True)),
                ('city', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
