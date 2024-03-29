# Generated by Django 3.2.11 on 2022-01-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variant_details', '0003_auto_20220121_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensemblvep',
            name='af_1000gp3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='af_1000gp3_afr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='af_1000gp3_amr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='af_1000gp3_eas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='af_1000gp3_eur',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='af_1000gp3_sas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='cadd_phred',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='cadd_raw',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='exac_adj_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='exac_afr_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='exac_amr_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='exac_eas_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='exac_nfe_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='exac_sas_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='gnomad_genomes_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='gnomad_genomes_afr_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='gnomad_genomes_eas_af',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemblvep',
            name='sift_score',
            field=models.TextField(blank=True, null=True),
        ),
    ]
