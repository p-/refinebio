# Generated by Django 2.1.8 on 2019-08-09 16:48

from django.db import migrations


def fix_typo_in_sample_manufacturer(apps, schema_editor):
    """Fixes affymetrix samples that have their manufacturer set to "AFFYMETRTIX" or "NEXTSEQ" """
    Sample = apps.get_model("data_refinery_common", "Sample")
    Sample.objects.all().filter(manufacturer="AFFYMETRTIX").update(manufacturer="AFFYMETRIX")
    Sample.objects.all().filter(manufacturer="NEXTSEQ").update(manufacturer="ILLUMINA")


class Migration(migrations.Migration):

    dependencies = [
        ("data_refinery_common", "0029_auto_20190809_1648"),
    ]

    operations = [
        migrations.RunPython(fix_typo_in_sample_manufacturer),
    ]
