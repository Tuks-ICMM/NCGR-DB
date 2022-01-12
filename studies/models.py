from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.
class Studies(Page):
    subpage_types = ["study_variants.StudyVariantsIndexPage"]

    doi = models.TextField(blank=True, null=True)  # Field name made lowercase.
    papers = models.TextField(blank=True, null=True)  # Field name made lowercase.
    study_population_description = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    unicef_regional_classification = models.TextField(
        blank=True, null=True
    )  # Field name made lowercase.
    methods = models.TextField(blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.papers

    content_panels = Page.content_panels + [
        FieldPanel("doi"),
        FieldPanel("papers"),
        FieldPanel("study_population_description"),
        FieldPanel("unicef_regional_classification"),
        FieldPanel("methods"),
    ]


class StudiesIndexPage(Page):
    subpage_types = ["studies.Studies"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["studies"] = Studies.objects.all()
        return context
