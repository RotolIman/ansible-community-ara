# Generated by Django 2.2.19 on 2021-07-07 19:57

from django.db import migrations, models
import django.db.models.deletion

def update_latest(apps, schema_editor):
    """ Computes the latest host for each host name to update the LatestHost table """
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    db_alias = schema_editor.connection.alias
    host_model = apps.get_model('api', 'Host')
    latesthost_model = apps.get_model('api', 'LatestHost')

    updated = []
    for host in host_model.objects.all():
        if host.name in updated:
            continue

        latest = host_model.objects.filter(name=host.name).order_by('-updated')[0]
        latesthost_model.objects.using(db_alias).create(name=host.name, host=latest)
        updated.append(host.name)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_playbook_controller'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestHost',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Host')),
            ],
            options={
                'db_table': 'latest_hosts',
            },
        ),
        migrations.RunPython(update_latest)
    ]
