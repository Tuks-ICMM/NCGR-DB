import sys

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, ParentalKey


# Create your models here.
class StudyVariants(models.Model):

    paper = ParentalKey(
        "studies.Studies",
        on_delete=models.SET_NULL,
        related_name="study_variants",
        null=True,
        blank=True,
    )  # Field name made lowercase.
    variant = ParentalKey(
        "variant_details.VariantDetails",
        on_delete=models.SET_NULL,
        related_name="study_variants",
        null=True,
        blank=True,
    )  # Field name made lowercase.
    reported_allele_or_genotype = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    condition = models.TextField(blank=True, null=True)  # Field name made lowercase.
    condition_description = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    disease_status = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    odds_ratio = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True
    )  # Field name made lowercase.
    p_value = models.DecimalField(
        max_digits=9, decimal_places=8, blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return str(self.odds_ratio)

    panels = [
        FieldPanel("variant"),
        FieldPanel("reported_allele_or_genotype"),
        FieldPanel("condition"),
        FieldPanel("condition_description"),
        FieldPanel("disease_status"),
        FieldPanel("odds_ratio"),
        FieldPanel("p_value"),
    ]
