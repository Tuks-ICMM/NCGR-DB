from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.
class Studies(models.Model):
    doi = models.TextField(
        db_column="DOI", blank=True, null=True
    )  # Field name made lowercase.
    papers = models.TextField(
        db_column="Papers", blank=True, null=True
    )  # Field name made lowercase.
    study_population_description = models.TextField(
        db_column="Study_population_description", blank=True, null=True
    )  # Field name made lowercase.
    unicef_regional_classification = models.TextField(
        db_column="UNICEF_regional_classification", blank=True, null=True
    )  # Field name made lowercase.
    methods = models.TextField(
        db_column="Methods", blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return self.papers

    class Meta:
        managed = False
        db_table = "studies"


class StudiesIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["studies"] = Studies.objects.all()
        return context
