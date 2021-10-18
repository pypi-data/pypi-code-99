# Generated by Django 3.2.4 on 2021-07-01 10:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpl', '0002_run_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(editable=False, max_length=32, unique=True)),
                ('last_used', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gameexperience',
            name='marketplace_key',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_key',
        ),
        migrations.RemoveField(
            model_name='run',
            name='marketplace_closed',
        ),
        migrations.RemoveField(
            model_name='run',
            name='marketplace_key',
        ),
        migrations.RemoveField(
            model_name='run',
            name='marketplace_open',
        ),
        migrations.AddField(
            model_name='run',
            name='managers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
