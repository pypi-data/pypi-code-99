# Generated by Django 2.2.12 on 2020-06-16 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0006_auto_20191213_0044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LogEntry',
        ),
        migrations.DeleteModel(
            name='UserMailerLogEntry',
        ),
    ]
