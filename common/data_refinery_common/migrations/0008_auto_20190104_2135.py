# Generated by Django 2.1.2 on 2019-01-04 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("data_refinery_common", "0007_auto_20190103_1555"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExperimentResultAssociation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "experiment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_refinery_common.Experiment",
                    ),
                ),
            ],
            options={"db_table": "experiment_result_associations",},
        ),
        migrations.AddField(
            model_name="computationalresult",
            name="samples",
            field=models.ManyToManyField(
                through="data_refinery_common.SampleResultAssociation",
                to="data_refinery_common.Sample",
            ),
        ),
        migrations.AddField(
            model_name="experimentresultassociation",
            name="result",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="data_refinery_common.ComputationalResult",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="experimentresultassociation", unique_together={("result", "experiment")},
        ),
    ]
