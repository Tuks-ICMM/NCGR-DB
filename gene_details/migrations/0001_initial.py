# Generated by Django 3.2.11 on 2022-01-11 08:09

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneDetails',
            fields=[
                ('gene', models.CharField(db_column='Gene', max_length=150, primary_key=True, serialize=False)),
                ('cytoband_position', models.TextField(blank=True, db_column='Cytoband_position', null=True)),
                ('omim', models.IntegerField(blank=True, db_column='OMIM', null=True)),
                ('rvis_score', models.DecimalField(blank=True, db_column='RVIS_score', decimal_places=2, max_digits=3, null=True)),
                ('rvis_percentage', models.DecimalField(blank=True, db_column='RVIS_percentage', decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneDetailsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GeneHpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.TextField(blank=True, db_column='Symbol', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('hpoid', models.TextField(blank=True, db_column='HPOId', null=True)),
                ('alternativeid', models.TextField(blank=True, db_column='AlternativeId', null=True)),
                ('definition', models.TextField(blank=True, db_column='Definition', null=True)),
                ('inputterm', models.ForeignKey(blank=True, db_column='InputTerm', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gene_inputterm', to='gene_details.genedetails')),
            ],
        ),
    ]
