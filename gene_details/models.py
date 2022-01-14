from django.db import models
from django.shortcuts import render
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class GeneDetails(Page):

    subpage_types = ["gene_details.GeneHpo"]

    template = ""
    gene = models.CharField(max_length=150)  # Field name made lowercase.
    cytoband_position = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    omim = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    rvis_score = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    rvis_percentage = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    def __str__(self):
        return self.gene

    content_panels = Page.content_panels + [
        FieldPanel("gene"),
        FieldPanel("cytoband_position"),
        FieldPanel("omim"),
        FieldPanel("rvis_score"),
        FieldPanel("rvis_percentage"),
    ]


class GeneHpo(Page):

    template = "genehpo_view.html"

    inputterm = models.ForeignKey(
        GeneDetails,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="gene_hpo",
    )  # Field name made lowercase.
    symbol = models.TextField(blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)  # Field name made lowercase.
    hpoid = models.TextField(blank=True, null=True)  # Field name made lowercase.
    alternativeid = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    definition = models.TextField(blank=True, null=True)  # Field name made lowercase.

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


class GeneDetailsIndexPage(RoutablePageMixin, Page):

    subpage_types = ["gene_details.GeneDetails"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context["genes"] = GeneDetails.objects.all()
    #     context["requested_hpo"] = GeneHpo.objects.all()
    #     return context

    @route(r"^$")
    def gene_index_page(self, request, *args, **kwargs):
        """View all the genes"""
        all_genes = GeneDetails.objects.all()
        return self.render(request, context_overrides={"genes": all_genes})

    @route(r"^(?P<gene_id>[A-Z0-9]+/{0,1})$")
    def selected_gene(self, request, gene_id, *args, **kwargs):
        """View a specific gene"""
        gene = GeneDetails.objects.get(gene_id=gene_id)
        return self.render(request, context_overrides={"genes": gene})
