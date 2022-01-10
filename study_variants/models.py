from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

import sys
sys.path.append('C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/variant_details')
import variant_details.models
sys.path.append('C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/studies')
import studies.models

# Create your models here.
class StudyVariants(models.Model):
    paper = models.ForeignKey(studies.models.Studies, models.PROTECT, db_column='Paper_id')  # Field name made lowercase.
    variant = models.ForeignKey(variant_details.models.VariantDetails, models.PROTECT, db_column='Variant_id')  # Field name made lowercase.
    variant_name = models.TextField(db_column='Variant_name')  # Field name made lowercase.
    reported_allele_or_genotype = models.TextField(db_column='Reported_allele_or_genotype', blank=True, null=True)  # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True, null=True)  # Field name made lowercase.
    condition_description = models.TextField(db_column='Condition_description', blank=True, null=True)  # Field name made lowercase.
    disease_status = models.TextField(db_column='Disease_status', blank=True, null=True)  # Field name made lowercase.
    odds_ratio = models.DecimalField(db_column='Odds_ratio', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    p_value = models.DecimalField(db_column='P_value', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_variants'

    def __str__(self):
        return self.variant_name

class StudyVariantsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['study_variants'] = StudyVariants.objects.all()
        return context