from django import template

register = template.Library()

@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, str):
        return text.startswith(starts)
    return False

@register.simple_tag(name="alfa_link")
def alfa_link(rsid: str):
    return f"https://www.ncbi.nlm.nih.gov/snp/{rsid}#frequency_tab"

