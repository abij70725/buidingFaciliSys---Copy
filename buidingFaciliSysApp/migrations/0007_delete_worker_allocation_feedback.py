# Generated by Django 5.1.3 on 2025-01-27 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buidingFaciliSysApp', '0006_remove_request_feedback_worker_allocation_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Worker_allocation_feedback',
        ),
    ]
