# Generated by Django 3.2.11 on 2022-03-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("variant_details", "0004_auto_20220124_1037"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ensemblvep",
            options={
                "verbose_name": "Variant effect predictions",
                "verbose_name_plural": "Variant effect predictions",
            },
        ),
        migrations.AlterModelOptions(
            name="mtvep",
            options={
                "verbose_name": "Variant effect predictions",
                "verbose_name_plural": "Variant effect predictions",
            },
        ),
        migrations.AlterModelOptions(
            name="variantdetails",
            options={"verbose_name": "Variant", "verbose_name_plural": "Variants"},
        ),
    ]
