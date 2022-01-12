from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

import sys

sys.path.append(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/NESHIE-DB/variant_details"
)
import variant_details.models

sys.path.append("C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/NESHIE-DB/mysite/studies")
import studies.models

# Create your models here.
class StudyVariants(Page):

    paper = models.ForeignKey(
        studies.models.Studies,
        models.PROTECT,
        related_name="study_variants",
    )  # Field name made lowercase.
    variant = models.ForeignKey(
        variant_details.models.VariantDetails,
        models.PROTECT,
    )  # Field name made lowercase.
    variant_name = models.TextField(blank=True, null=True)  # Field name made lowercase.
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
        max_digits=5, decimal_places=4, blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return self.variant_name

    content_panels = Page.content_panels + [
        FieldPanel("paper"),
        FieldPanel("variant"),
        FieldPanel("variant_name"),
        FieldPanel("reported_allele_or_genotype"),
        FieldPanel("condition"),
        FieldPanel("condition_description"),
        FieldPanel("disease_status"),
        FieldPanel("odds_ratio"),
        FieldPanel("p_value"),
    ]


class StudyVariantsIndexPage(Page):
    subpage_types = ["study_variants.StudyVariants"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request):
        context = super().get_context(request)
        context["study_variants"] = StudyVariants.objects.all()
        return context
