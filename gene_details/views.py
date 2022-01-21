# from django.shortcuts import render
# import sys

# sys.path.append("C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/NESHIE-DB/gene_details")
# import gene_details.models
# from django.http import HttpResponse
# import csv

# # Create your views here.
# def genehpo_view(request, gene):
#     if gene_details.models.GeneHpo.objects.filter(inputterm=gene.upper()) != None:
#         hpo = gene_details.models.GeneHpo.objects.filter(inputterm=gene.upper())
#         return render(
#             request, "gene_details/genehpo_view.html", {"hpo": hpo, "gene": gene}
#         )
#     else:
#         return render(request, "404.html")


# def export_genedetails_csv(request):
#     response = HttpResponse(content_type="text/csv")
#     response["Content-Disposition"] = 'attachment; filename="genedetails.csv"'

#     writer = csv.writer(response)
#     writer.writerow(
#         [
#             "gene",
#             "cytoband_position",
#             "omim",
#             "rvis_score",
#             "rvis_percentage",
#         ]
#     )

#     genes = gene_details.models.GeneDetails.objects.all().values_list(
#         "gene",
#         "cytoband_position",
#         "omim",
#         "rvis_score",
#         "rvis_percentage",
#     )
#     for gene in genes:
#         writer.writerow(gene)

#     return response
