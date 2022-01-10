from django.shortcuts import render
from .models import HpoFilter
import sys

sys.path.append(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/gene_details"
)
import gene_details.models

# Create your views here.
def hpo_list(request):
    f = HpoFilter(request.GET, queryset=gene_details.models.GeneHpo.objects.all())
    return render(request, "home/hpo_list.html", {"filter": f})
