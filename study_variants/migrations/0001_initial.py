# Generated by Django 3.2.5 on 2022-01-07 08:23

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudyVariants",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("variant_name", models.TextField(db_column="Variant_name")),
                (
                    "reported_allele_or_genotype",
                    models.TextField(
                        blank=True, db_column="Reported_allele_or_genotype", null=True
                    ),
                ),
                (
                    "condition",
                    models.TextField(blank=True, db_column="Condition", null=True),
                ),
                (
                    "condition_description",
                    models.TextField(
                        blank=True, db_column="Condition_description", null=True
                    ),
                ),
                (
                    "disease_status",
                    models.TextField(blank=True, db_column="Disease_status", null=True),
                ),
                (
                    "odds_ratio",
                    models.DecimalField(
                        blank=True,
                        db_column="Odds_ratio",
                        decimal_places=3,
                        max_digits=5,
                        null=True,
                    ),
                ),
                (
                    "p_value",
                    models.DecimalField(
                        blank=True,
                        db_column="P_value",
                        decimal_places=4,
                        max_digits=5,
                        null=True,
                    ),
                ),
            ],
            options={"db_table": "study_variants", "managed": False,},
        ),
        migrations.CreateModel(
            name="StudyVariantsIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
    ]