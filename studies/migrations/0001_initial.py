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
            name="Studies",
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
                ("doi", models.TextField(blank=True, db_column="DOI", null=True)),
                ("papers", models.TextField(blank=True, db_column="Papers", null=True)),
                (
                    "study_population_description",
                    models.TextField(
                        blank=True, db_column="Study_population_description", null=True
                    ),
                ),
                (
                    "unicef_regional_classification",
                    models.TextField(
                        blank=True,
                        db_column="UNICEF_regional_classification",
                        null=True,
                    ),
                ),
                (
                    "methods",
                    models.TextField(blank=True, db_column="Methods", null=True),
                ),
            ],
            options={"db_table": "studies", "managed": False,},
        ),
        migrations.CreateModel(
            name="StudiesIndexPage",
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