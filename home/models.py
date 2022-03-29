import sys

import django_filters
from django.db import models
from studies.models import StudiesIndexPage
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from home import blocks

sys.path.append(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/gene_details"
)
import gene_details.models

sys.path.append(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/study_variants"
)
import study_variants.models


class HomePage(Page):
    max_count = 1

    parent_page_types = ["wagtailcore.Page"]

    subpage_types = [
        "gene_details.GeneDetailsIndexPage",
        "studies.StudiesIndexPage",
        "variant_details.VariantDetailsIndexPage",
    ]

    body = RichTextField(blank=True)
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    about = RichTextField(blank=True)

    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
            ("affiliation_cards", blocks.AffiliationBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        ImageChooserPanel("header_image"),
        FieldPanel("about"),
        StreamFieldPanel("content"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["all_studies"] = StudiesIndexPage.objects.get()
        context["genes"] = gene_details.models.GeneDetails.objects.all()
        context["hpo"] = gene_details.models.GeneHpo.objects.all()
        context["study_variants"] = study_variants.models.StudyVariants.objects.values(
            "condition"
        ).distinct()
        return context
