# Generated by Django 2.2.9 on 2019-12-23 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_refinery_common", "0050_remove_organismindex_s3_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dataset",
            name="email_sent",
        ),
    ]
