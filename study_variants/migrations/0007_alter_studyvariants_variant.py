# Generated by Django 3.2.11 on 2022-01-25 14:00

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('variant_details', '0004_auto_20220124_1037'),
        ('study_variants', '0006_alter_studyvariants_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyvariants',
            name='variant',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='study_variants', to='variant_details.variantdetails'),
        ),
    ]
