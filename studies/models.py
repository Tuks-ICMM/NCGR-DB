from django.db import models
from django.http import JsonResponse
from gene_details.models import GeneDetails
from study_variants.models import StudyVariants
from variant_details.models import VariantDetails
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class Studies(Page):

    parent_page_types = ["studies.StudiesIndexPage"]

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
        MultiFieldPanel(
            [
                FieldPanel("doi"),
                FieldPanel("papers"),
                FieldPanel("study_population_description"),
                FieldPanel("unicef_regional_classification"),
                FieldPanel("methods"),
            ],
            heading="Study",
        ),
        MultiFieldPanel([InlinePanel("study_variants")], heading="Study variants"),
    ]

    def __str__(self):
        return self.papers

    class Meta:
        verbose_name = "Study"
        verbose_name_plural = "Studies"


class StudiesIndexPage(RoutablePageMixin, Page):

    max_count = 1

    parent_page_types = ["home.HomePage"]
    subpage_types = ["studies.Studies"]

    intro = RichTextField(blank=True)
    study_findings_intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("study_findings_intro"),
    ]

    @route(r"^$")
    def studies_index_page(self, request, *args, **kwargs):
        """View all the studies"""
        all_studies = Studies.objects.all()
        return self.render(
            request,
            context_overrides={"all_studies": all_studies},
            template="studies/studies_index_page.html",
        )

    @route(r"(?P<slug>[0-9a-zA-Z-_]+)[\/]{0,1}")
    def selected_study(self, request, slug, *args, **kwargs):
        """View a specific gene"""
        study = Studies.objects.get(slug=slug)
        study_variants = StudyVariants.objects.filter(paper=study)
        return self.render(
            request,
            template="studies/selected_study.html",
            context_overrides={"study": study, "study_variants": study_variants},
        )
