from django import template
from gene_details.models import GeneDetails
from studies.models import Studies

register = template.Library()


@register.filter("pub_count")
def pub_count(gene: GeneDetails):
    if isinstance(gene, GeneDetails):
        return (
            Studies.objects.filter(study_variants__variant__gene=gene)
            .distinct()
            .count()
        )
    return False
