from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

import sys

sys.path.append("C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/NESHIE-DB/gene_details")
import gene_details.models

# Create your models here.
class VariantDetails(Page):

    subpage_types = ['variant_details.EnsemblVep', 'variant_details.MtVep']

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
    disease_association_with_ref_allele = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    variant_type = models.TextField(blank=True, null=True)  # Field name made lowercase.
    gene = models.ForeignKey(
        gene_details.models.GeneDetails, models.PROTECT, related_name="variant_details"
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant_name

    content_panels = Page.content_panels + [
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
        FieldPanel("gene"),
    ]


class EnsemblVep(Page):
    variant = models.ForeignKey(
        "VariantDetails", models.CASCADE, related_name="ensembl_vep"
    )  # Field name made lowercase.
    variant_name = models.TextField(blank=True, null=True)  # Field name made lowercase.
    ensembl_canonical_hgvsc = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consequence_terms = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    af_1000gp3_eur = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3 = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    af_1000gp3_afr = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_amr = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_sas = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_eas = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exac_adj_af = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_afr_af = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_amr_af = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_eas_af = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_nfe_af = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_sas_af = models.DecimalField(
        max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    gnomad_genomes_af = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gnomad_genomes_afr_af = models.DecimalField(
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gnomad_genomes_eas_af = models.DecimalField(
        max_digits=10,
        decimal_places=9,
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
    sift_score = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    sift_prediction = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    cadd_raw = models.DecimalField(
        max_digits=7, decimal_places=6, blank=True, null=True
    )  # Field name made lowercase.
    cadd_phred = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant

    content_panels = Page.content_panels + [
        FieldPanel("variant"),
        FieldPanel("variant_name"),
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


class MtVep(Page):
    variant = models.ForeignKey(
        "VariantDetails", models.CASCADE, related_name="mtveps"
    )  # Field name made lowercase.
    variant_name = models.TextField(null=True, blank=True)  # Field name made lowercase.
    reference_genome = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    chromosome = models.TextField(blank=True, null=True)  # Field name made lowercase.
    genomic_start_position = models.IntegerField(
        blank=True, null=True
    )  # Field name made lowercase.
    genomic_end_position = models.IntegerField(
        blank=True, null=True
    )  # Field name made lowercase.
    reference_allele = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    alternate_allele = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    query_chr = models.TextField(blank=True, null=True)  # Field name made lowercase.
    query_genomic_start_pos = models.IntegerField(
        blank=True, null=True
    )  # Field name made lowercase.
    query_ref = models.TextField(blank=True, null=True)  # Field name made lowercase.
    query_alt = models.TextField(blank=True, null=True)  # Field name made lowercase.
    query_transcript_stable = models.TextField(
        blank=True, null=True
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

    content_panels = Page.content_panels + [
        FieldPanel("variant"),
        FieldPanel("variant_name"),
        FieldPanel("reference_genome"),
        FieldPanel("chromosome"),
        FieldPanel("genomic_start_position"),
        FieldPanel("genomic_end_position"),
        FieldPanel("reference_allele"),
        FieldPanel("alternate_allele"),
        FieldPanel("query_chr"),
        FieldPanel("query_genomic_start_pos"),
        FieldPanel("query_ref"),
        FieldPanel("query_alt"),
        FieldPanel("query_transcript_stable"),
        FieldPanel("query_ncbi_geneid"),
        FieldPanel("query_prediction"),
        FieldPanel("query_model"),
    ]


class VariantDetailsIndexPage(Page):
    subpage_types = ['variant_details.VariantDetails']

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["variants"] = VariantDetails.objects.all()
        return context
