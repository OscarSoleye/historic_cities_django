# Generated by Django 4.1.7 on 2023-03-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('city', models.TextField()),
                ('otherName', models.TextField()),
                ('country', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('year', models.TextField()),
                ('pop', models.TextField()),
                ('city_id', models.TextField()),
            ],
        ),
    ]
