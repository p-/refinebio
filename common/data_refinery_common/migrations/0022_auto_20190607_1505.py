# Generated by Django 2.1.8 on 2019-06-07 15:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_refinery_common', '0021_experiment_num_downloadable_samples'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='aggregate_by',
            field=models.CharField(choices=[('ALL', 'All'), ('EXPERIMENT', 'Experiment'), ('SPECIES', 'Species')], default='EXPERIMENT', help_text='Specifies how samples are [aggregated](http://docs.refine.bio/en/latest/main_text.html#aggregations).', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, help_text="This is a dictionary where the keys are experiment accession codes and the values are lists with sample accession codes. Eg: `{'E-ABC-1': ['SAMP1', 'SAMP2']}`"),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='quantile_normalize',
            field=models.BooleanField(default=True, help_text='Part of the advanced options. Allows [skipping quantile normalization](http://docs.refine.bio/en/latest/faq.html#what-does-it-mean-to-skip-quantile-normalization-for-rna-seq-samples) for RNA-Seq samples.'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='scale_by',
            field=models.CharField(choices=[('NONE', 'None'), ('MINMAX', 'Minmax'), ('STANDARD', 'Standard'), ('ROBUST', 'Robust')], default='NONE', help_text='Specifies options for [transformations](http://docs.refine.bio/en/latest/main_text.html#transformations).', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='size_in_bytes',
            field=models.BigIntegerField(blank=True, default=0, help_text='Contains the size in bytes of the processed dataset.', null=True),
        ),
    ]