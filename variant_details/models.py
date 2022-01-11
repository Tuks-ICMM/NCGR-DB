from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

import sys

sys.path.append(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/gene_details"
)
import gene_details.models

# Create your models here.
class VariantDetails(models.Model):
    variant_name = models.CharField(
        db_column="Variant_name", max_length=150
    )  # Field name made lowercase.
    reference_genome = models.TextField(
        db_column="Reference_genome", blank=True, null=True
    )  # Field name made lowercase.
    transcript_id = models.TextField(
        db_column="Transcript_ID", blank=True, null=True
    )  # Field name made lowercase.
    chromosome = models.TextField(
        db_column="Chromosome", blank=True, null=True
    )  # Field name made lowercase.
    genomic_start_position = models.TextField(
        db_column="Genomic_start_position", blank=True, null=True
    )  # Field name made lowercase.
    genomic_end_position = models.TextField(
        db_column="Genomic_end_position", blank=True, null=True
    )  # Field name made lowercase.
    reference_allele = models.TextField(
        db_column="Reference_allele", blank=True, null=True
    )  # Field name made lowercase.
    alternate_allele = models.TextField(
        db_column="Alternate_allele", blank=True, null=True
    )  # Field name made lowercase.
    disease_association_with_ref_allele = models.TextField(
        db_column="Disease_association_with_ref_allele", blank=True, null=True
    )  # Field name made lowercase.
    variant_type = models.TextField(
        db_column="Variant_type", blank=True, null=True
    )  # Field name made lowercase.
    gene = models.ForeignKey(
        gene_details.models.GeneDetails, models.PROTECT, db_column="Gene"
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant_name

    class Meta:
        managed = False
        db_table = "variant_details"


class EnsemblVep(models.Model):
    variant = models.ForeignKey(
        "VariantDetails", models.CASCADE, db_column="Variant_id"
    )  # Field name made lowercase.
    variant_name = models.TextField(
        db_column="Variant_name"
    )  # Field name made lowercase.
    ensembl_canonical_hgvsc = models.TextField(
        db_column="Ensembl canonical HGVSC", blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consequence_terms = models.TextField(
        db_column="Consequence_terms", blank=True, null=True
    )  # Field name made lowercase.
    af_1000gp3_eur = models.DecimalField(
        db_column="AF_1000gp3_EUR",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3 = models.DecimalField(
        db_column="AF_1000gp3", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    af_1000gp3_afr = models.DecimalField(
        db_column="AF_1000gp3_afr",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_amr = models.DecimalField(
        db_column="AF_1000gp3_amr",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_sas = models.DecimalField(
        db_column="AF_1000gp3_SAS",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    af_1000gp3_eas = models.DecimalField(
        db_column="AF_1000gp3_EAS",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    exac_adj_af = models.DecimalField(
        db_column="Exac_ADJ_AF", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_afr_af = models.DecimalField(
        db_column="Exac_AFR_AF", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_amr_af = models.DecimalField(
        db_column="Exac_AMR_AF", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_eas_af = models.DecimalField(
        db_column="Exac_EAS_AF", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_nfe_af = models.DecimalField(
        db_column="Exac_NFE_AF", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    exac_sas_af = models.DecimalField(
        db_column="Exac_SAS_AF", max_digits=10, decimal_places=9, blank=True, null=True
    )  # Field name made lowercase.
    gnomad_genomes_af = models.DecimalField(
        db_column="GnomAD_genomes_af",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gnomad_genomes_afr_af = models.DecimalField(
        db_column="GnomAD_genomes_afr_af",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gnomad_genomes_eas_af = models.DecimalField(
        db_column="GnomAD_genomes_eas_af",
        max_digits=10,
        decimal_places=9,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    study_acmg = models.TextField(
        db_column="Study_ACMG", blank=True, null=True
    )  # Field name made lowercase.
    polyphen2_hvar_score = models.TextField(
        db_column="Polyphen2_hvar_score", blank=True, null=True
    )  # Field name made lowercase.
    polyphen2_hvar_pred = models.TextField(
        db_column="Polyphen2_hvar_pred", blank=True, null=True
    )  # Field name made lowercase.
    sift4g_score = models.TextField(
        db_column="Sift4G_score", blank=True, null=True
    )  # Field name made lowercase.
    sift4g_pred = models.TextField(
        db_column="Sift4G_pred", blank=True, null=True
    )  # Field name made lowercase.
    fathmm_score = models.TextField(
        db_column="Fathmm_score", blank=True, null=True
    )  # Field name made lowercase.
    fathmm_pred = models.TextField(
        db_column="Fathmm_pred", blank=True, null=True
    )  # Field name made lowercase.
    sift_score = models.DecimalField(
        db_column="Sift_score", max_digits=3, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    sift_prediction = models.TextField(
        db_column="Sift_prediction", blank=True, null=True
    )  # Field name made lowercase.
    cadd_raw = models.DecimalField(
        db_column="CADD_raw", max_digits=7, decimal_places=6, blank=True, null=True
    )  # Field name made lowercase.
    cadd_phred = models.DecimalField(
        db_column="CADD_phred", max_digits=5, decimal_places=3, blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant

    class Meta:
        managed = False
        db_table = "ensembl_vep"


class MtVep(models.Model):
    variant = models.ForeignKey(
        "VariantDetails", models.CASCADE, db_column="Variant_id"
    )  # Field name made lowercase.
    variant_name = models.TextField(
        db_column="Variant_name"
    )  # Field name made lowercase.
    reference_genome = models.TextField(
        db_column="Reference_genome", blank=True, null=True
    )  # Field name made lowercase.
    chromosome = models.TextField(
        db_column="Chromosome", blank=True, null=True
    )  # Field name made lowercase.
    genomic_start_position = models.IntegerField(
        db_column="Genomic_start_position", blank=True, null=True
    )  # Field name made lowercase.
    genomic_end_position = models.IntegerField(
        db_column="Genomic_end_position", blank=True, null=True
    )  # Field name made lowercase.
    reference_allele = models.TextField(
        db_column="Reference_allele", blank=True, null=True
    )  # Field name made lowercase.
    alternate_allele = models.TextField(
        db_column="Alternate_allele", blank=True, null=True
    )  # Field name made lowercase.
    query_chr = models.TextField(
        db_column="Query_chr", blank=True, null=True
    )  # Field name made lowercase.
    query_genomic_start_pos = models.IntegerField(
        db_column="Query_genomic_start_pos", blank=True, null=True
    )  # Field name made lowercase.
    query_ref = models.TextField(
        db_column="Query_ref", blank=True, null=True
    )  # Field name made lowercase.
    query_alt = models.TextField(
        db_column="Query_alt", blank=True, null=True
    )  # Field name made lowercase.
    query_transcript_stable = models.TextField(
        db_column="Query_transcript_stable", blank=True, null=True
    )  # Field name made lowercase.
    query_ncbi_geneid = models.TextField(
        db_column="Query_NCBI_geneid", blank=True, null=True
    )  # Field name made lowercase.
    query_prediction = models.TextField(
        db_column="Query_prediction", blank=True, null=True
    )  # Field name made lowercase.
    query_model = models.TextField(
        db_column="Query_model", blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant

    class Meta:
        managed = False
        db_table = "mt_vep"


class VariantDetailsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro", classname="full")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["variants"] = VariantDetails.objects.all()
        return context
