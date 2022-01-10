from django.shortcuts import render
from .models import GeneHpo

# Create your views here.
def genehpo_view(request, gene):
    if GeneHpo.objects.filter(inputterm=gene.upper()) != None:
        hpo = GeneHpo.objects.filter(inputterm=gene.upper())
        return render(
            request, "gene_details/genehpo_view.html", {"hpo": hpo, "gene": gene}
        )
    else:
        return render(request, "404.html")
