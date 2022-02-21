from django import template
from gene_details.models import GeneDetailsIndexPage
from home.models import HomePage
from studies.models import StudiesIndexPage
from variant_details.models import VariantDetailsIndexPage

register = template.Library()


class LoadIndexPages(template.Node):
    def render(self, context):
        context["home_page"] = HomePage.objects.get()
        context["studies_page"] = StudiesIndexPage.objects.get()
        context["variants_page"] = VariantDetailsIndexPage.objects.get()
        context["genes_page"] = GeneDetailsIndexPage.objects.get()
        return ""


@register.tag
def load_page(self, request):
    return LoadIndexPages()
