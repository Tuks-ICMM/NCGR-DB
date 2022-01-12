from django.shortcuts import render
from .models import MtVep, EnsemblVep

# Create your views here.
def vep_view(request, variant_name):
    ensembl_vep = EnsemblVep.objects.filter(variant_name=variant_name)
    mt_vep = MtVep.objects.filter(variant_name=variant_name)
    return render(
        request,
        "variant_details/vep_view.html",
        {
            "variant_name": variant_name,
            "mt_vep": mt_vep,
            "ensembl_vep": ensembl_vep,
        },
    )
