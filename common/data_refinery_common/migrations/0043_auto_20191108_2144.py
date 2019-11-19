# Generated by Django 2.1.8 on 2019-11-08 21:44

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('data_refinery_common', '0042_remove_experiment_organism_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompendiumResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant_sf_only', models.BooleanField(default=False)),
                ('compendium_version', models.IntegerField(blank=True, null=True)),
                ('svd_algorithm', models.CharField(choices=[('NONE', 'None'), ('RANDOMIZED', 'randomized'), ('ARPACK', 'arpack')], default='NONE', help_text='The SVD algorithm that was used to impute the compendium result.', max_length=255)),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'compendium_results',
                'base_manager_name': 'public_objects',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('public_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CompendiumResultOrganismAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compendium_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_refinery_common.CompendiumResult')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_refinery_common.Organism')),
            ],
            options={
                'db_table': 'compendium_result_organism_associations',
            },
        ),
        migrations.AddField(
            model_name='compendiumresult',
            name='organisms',
            field=models.ManyToManyField(related_name='compendium_results', through='data_refinery_common.CompendiumResultOrganismAssociation', to='data_refinery_common.Organism'),
        ),
        migrations.AddField(
            model_name='compendiumresult',
            name='primary_organism',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_compendium_results', to='data_refinery_common.Organism'),
        ),
        migrations.AddField(
            model_name='compendiumresult',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compendium_result', to='data_refinery_common.ComputationalResult'),
        ),
        migrations.AlterUniqueTogether(
            name='compendiumresultorganismassociation',
            unique_together={('compendium_result', 'organism')},
        ),
    ]