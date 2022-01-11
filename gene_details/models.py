from django.db import models
from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route


# Create your models here.
class GeneDetails(models.Model):

    gene = models.CharField(
        db_column="Gene", primary_key=True, max_length=150
    )  # Field name made lowercase.
    cytoband_position = models.TextField(
        db_column="Cytoband_position", blank=True, null=True
    )  # Field name made lowercase.
    omim = models.IntegerField(
        db_column="OMIM", blank=True, null=True
    )  # Field name made lowercase.
    rvis_score = models.DecimalField(
        db_column="RVIS_score", max_digits=3, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    rvis_percentage = models.DecimalField(
        db_column="RVIS_percentage",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    def __str__(self):
        return self.gene

    class Meta:
        managed = False
        db_table = "gene_details"


class GeneHpo(models.Model):

    # template = "genehpo_view.html"

    inputterm = models.ForeignKey(
        GeneDetails,
        models.SET_NULL,
        db_column="InputTerm",
        blank=True,
        null=True,
        related_name="gene_inputterm",
    )  # Field name made lowercase.
    symbol = models.TextField(
        db_column="Symbol", blank=True, null=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase.
    hpoid = models.TextField(
        db_column="HPOId", blank=True, null=True
    )  # Field name made lowercase.
    alternativeid = models.TextField(
        db_column="AlternativeId", blank=True, null=True
    )  # Field name made lowercase.
    definition = models.TextField(
        db_column="Definition", blank=True, null=True
    )  # Field name made lowercase.

    content_panels = Page.content_panels + [
        FieldPanel("inputterm"),
        FieldPanel("symbol"),
        FieldPanel("name"),
        FieldPanel("hpoid"),
        FieldPanel("alternativeid"),
        FieldPanel("definition"),
    ]

    def __str__(self):
        return self.symbol

    @property
    def all_hpo(self):
        """Returns all hpo terms except where null"""
        return GeneHpo.objects.exclude(name__isnull=True)

    class Meta:
        managed = False
        db_table = "gene_hpo"


class GeneDetailsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["genes"] = GeneDetails.objects.all()
        context["requested_hpo"] = GeneHpo.objects.all()
        return context
