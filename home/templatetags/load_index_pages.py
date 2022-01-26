from django import template
from studies.models import StudiesIndexPage

register = template.Library()


class LoadIndexPages(template.Node):
    def Render(self, context):
        context["studies_page"] = StudiesIndexPage.objects.get()
        return ""
