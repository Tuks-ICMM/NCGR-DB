# Generated by Django 4.0.4 on 2022-10-07 13:00

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gene_details', '0005_auto_20220329_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='genedetailsindexpage',
            name='gene_hpo_intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]