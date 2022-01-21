import sys

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

sys.path.append("C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/NESHIE-DB/gene_details")
import gene_details.models


# Create your models here.
class VariantDetails(Page):

    parent_page_types = ["variant_details.VariantDetailsIndexPage"]

    variant_name = models.CharField(max_length=150)  # Field name made lowercase.
    reference_genome = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    transcript_id = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    chromosome = models.TextField(blank=True, null=True)  # Field name made lowercase.
    genomic_start_position = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    genomic_end_position = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    reference_allele = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    alternate_allele = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    disease_association_with_ref_allele = models.BooleanField(
        blank=True, null=True
    )  # Field name made lowercase.
    variant_type = models.TextField(blank=True, null=True)  # Field name made lowercase.
    gene = ParentalKey(
        gene_details.models.GeneDetails,
        on_delete=models.SET_NULL,
        related_name="variant_details",
        null=True,
        blank=True,
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant_name

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("variant_name"),
                FieldPanel("reference_genome"),
                FieldPanel("transcript_id"),
                FieldPanel("chromosome"),
                FieldPanel("genomic_start_position"),
                FieldPanel("genomic_end_position"),
                FieldPanel("reference_allele"),
                FieldPanel("alternate_allele"),
                FieldPanel("disease_association_with_ref_allele"),
                FieldPanel("variant_type"),
            ],
            heading="Variant details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("gene"),
            ],
            heading="Gene",
        ),
        MultiFieldPanel(
            [
                InlinePanel("ensembl_vep"),
            ],
            heading="Ensembl VEP",
        ),
        MultiFieldPanel(
            [
                InlinePanel("mt_vep"),
            ],
            heading="MutationTaster VEP",
        ),
    ]


class EnsemblVep(models.Model):

    variant = ParentalKey(
        "variant_details.VariantDetails",
        on_delete=models.SET_NULL,
        related_name="ensembl_vep",
        null=True,
        blank=True,
    )  # Field name made lowercase. # Field name made lowercase.
    ensembl_canonical_hgvsc = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consequence_terms = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    af_1000gp3_eur = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3 = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    af_1000gp3_afr = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_amr = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_sas = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_eas = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exac_adj_af = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    exac_afr_af = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    exac_amr_af = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    exac_eas_af = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    exac_nfe_af = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    exac_sas_af = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    gnomad_genomes_af = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gnomad_genomes_afr_af = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gnomad_genomes_eas_af = models.FloatField(
        blank=True,
        null=True,
    )  # Field name made lowercase.
    study_acmg = models.TextField(blank=True, null=True)  # Field name made lowercase.
    polyphen2_hvar_score = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    polyphen2_hvar_pred = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    sift4g_score = models.TextField(blank=True, null=True)  # Field name made lowercase.
    sift4g_pred = models.TextField(blank=True, null=True)  # Field name made lowercase.
    fathmm_score = models.TextField(blank=True, null=True)  # Field name made lowercase.
    fathmm_pred = models.TextField(blank=True, null=True)  # Field name made lowercase.
    sift_score = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    sift_prediction = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    cadd_raw = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    cadd_phred = models.FloatField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.variant

    panels = [
        FieldPanel("variant"),
        FieldPanel("ensembl_canonical_hgvsc"),
        FieldPanel("consequence_terms"),
        FieldPanel("af_1000gp3_eur"),
        FieldPanel("af_1000gp3"),
        FieldPanel("af_1000gp3_afr"),
        FieldPanel("af_1000gp3_amr"),
        FieldPanel("af_1000gp3_sas"),
        FieldPanel("af_1000gp3_eas"),
        FieldPanel("exac_adj_af"),
        FieldPanel("exac_afr_af"),
        FieldPanel("exac_amr_af"),
        FieldPanel("exac_eas_af"),
        FieldPanel("exac_nfe_af"),
        FieldPanel("exac_sas_af"),
        FieldPanel("gnomad_genomes_af"),
        FieldPanel("gnomad_genomes_afr_af"),
        FieldPanel("gnomad_genomes_eas_af"),
        FieldPanel("study_acmg"),
        FieldPanel("polyphen2_hvar_score"),
        FieldPanel("polyphen2_hvar_pred"),
        FieldPanel("sift4g_score"),
        FieldPanel("sift4g_pred"),
        FieldPanel("fathmm_score"),
        FieldPanel("fathmm_pred"),
        FieldPanel("sift_score"),
        FieldPanel("sift_prediction"),
        FieldPanel("cadd_raw"),
        FieldPanel("cadd_phred"),
    ]


class MtVep(models.Model):

    variant = ParentalKey(
        "variant_details.VariantDetails",
        on_delete=models.SET_NULL,
        related_name="mt_vep",
        null=True,
        blank=True,
    )  # Field name made lowercase.
    query_ncbi_geneid = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    query_prediction = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    query_model = models.TextField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.variant

    panels = [
        FieldPanel("variant"),
        FieldPanel("query_ncbi_geneid"),
        FieldPanel("query_prediction"),
        FieldPanel("query_model"),
    ]


class VariantDetailsIndexPage(RoutablePageMixin, Page):

    max_count = 1

    parent_page_types = ["home.HomePage"]

    subpage_types = ["variant_details.VariantDetails"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["variants"] = VariantDetails.objects.all()
        return context

    @route(r"^$")
    def variant_index_page(self, request, *args, **kwargs):
        """View all the study variants"""
        variants = VariantDetails.objects.all()
        return self.render(request, context_overrides={"variants": variants})

    @route(r"^(?P<variant_id>./{0,1})$")
    def selected_variant(self, request, variant_id, *args, **kwargs):
        """View a specific study variant"""
        variant = VariantDetails.objects.get(variant_id=variant_id)
        return self.render(request, context_overrides={"variant": variant})
