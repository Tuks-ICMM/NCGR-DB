# Generated by Django 3.2.11 on 2022-01-19 11:52

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyVariants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_allele_or_genotype', models.TextField(blank=True, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('condition_description', models.TextField(blank=True, null=True)),
                ('disease_status', models.TextField(blank=True, null=True)),
                ('odds_ratio', models.IntegerField(blank=True, null=True)),
                ('p_value', models.IntegerField(blank=True, null=True)),
                ('paper', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='study_variants', to='studies.studies')),
            ],
        ),
    ]
