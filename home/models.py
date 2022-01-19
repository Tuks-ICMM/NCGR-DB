import sys

import django_filters
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

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

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['filter'] = HpoFilter(self.request.GET, queryset = self.get_queryset())
    #     return context

    # @property
    # def all_genes(self):
    #     """Returns all hpo terms except where null"""
    #     return GeneDetails.objects.exclude(name__isnull=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["genes"] = gene_details.models.GeneDetails.objects.all()
        context["hpo"] = gene_details.models.GeneHpo.objects.all()
        context["study_variants"] = study_variants.models.StudyVariants.objects.values(
            "condition"
        ).distinct()
        return context


# class HpoFilter(django_filters.FilterSet):
#     class Meta:
#         model = gene_details.models.GeneHpo
#         """Can make this a foreign key related name"""
#         fields = ["name"]


# @property
# def qs(self):
#     """Returns all hpo terms except where null"""
#     parent = super().qs
#     name = getattr(self.request, 'name', None)
#     return parent.filter(name__isnull=True)
