# from .models import HpoFilter
import sys

import gene_details.models
import study_variants.models
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

from .forms import filter_form

# Create your views here.
# def hpo_list(request):
#     f = HpoFilter(request.GET, queryset=gene_details.models.GeneHpo.objects.all())
#     return render(request, "home/hpo_list.html", {"filter": f})


# def filter_view(request):
#     form = filter_form()
#     all_study_variants = study_variants.models.StudyVariants.objects.all()
#     if request.method == "POST":
#         if form.is_valid():
#             conditions = form.cleaned_data["conditions"]
#             filtered_studyvariants = study_variants.models.StudyVariants.objects.all()
#             if conditions:
#                 filtered_studyvariants = filtered_studyvariants.filter(
#                     condition=conditions
#                 )
#             return render(
#                 request,
#                 "home/filter_view.html",
#                 {
#                     "form": form,
#                     "filtered_studyvariants": filtered_studyvariants,
#                 },
#             )
#     return render(
#         request,
#         "home/home_page.html",
#         {
#             "form": form,
#             "study_variants": study_variants,
#         },
#     )


def filter_view(request):
    form = filter_form()
    all_study_variants = study_variants.models.StudyVariants.objects.all()
    if request.method == "POST":
        if form.is_valid():
            conditions = form.cleaned_data["conditions"]
            if conditions:
                filtered_studyvariants = all_study_variants.filter(condition=conditions)
            return render(
                request,
                "filter_view.html",
                {
                    "form": form,
                    "filtered_studyvariants": filtered_studyvariants,
                },
            )
    else:
        form = filter_form()
        return render(
            request,
            "home_page.html",
            {
                "form": form,
                "all_study_variants": all_study_variants,
            },
        )
