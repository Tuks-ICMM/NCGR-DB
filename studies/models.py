from django.db import models
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


class StudiesIndexPage(RoutablePageMixin, Page):

    max_count = 1

    parent_page_types = ["home.HomePage"]
    subpage_types = ["studies.Studies"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context["studies"] = Studies.objects.all()
    #     return context

    @route(r"^$")
    def studies_index_page(self, request, *args, **kwargs):
        """View all the studies"""
        all_studies = Studies.objects.all()
        return self.render(request, context_overrides={"all_studies": all_studies})

    @route(r"^(?P<doi>^10.\d{4,9}/[-._;()/:a-z0-9A-Z]+/{0,1})$")
    def selected_study(self, request, doi, *args, **kwargs):
        """View a specific gene"""
        study = Studies.objects.get(doi=doi)
        return self.render(request, context_overrides={"studies": study})
