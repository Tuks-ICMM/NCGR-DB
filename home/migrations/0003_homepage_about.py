# Generated by Django 3.2.11 on 2022-03-22 13:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]