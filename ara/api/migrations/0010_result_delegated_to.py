# Generated by Django 2.2.24 on 2021-07-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_latesthost'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='delegated_to',
            field=models.ManyToManyField(to='api.Host'),
        ),
    ]
