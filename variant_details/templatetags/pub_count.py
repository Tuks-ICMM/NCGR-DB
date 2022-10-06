from django import template
from studies.models import Studies
from variant_details.models import VariantDetails

register = template.Library()


@register.filter("pub_count")
def pub_count(variant: VariantDetails):
    if isinstance(variant, VariantDetails):
        return (
            Studies.objects.filter(study_variants__variant=variant).distinct().count()
        )
    return False
