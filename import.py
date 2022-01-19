import pandas as pd

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/studies.xlsx"
)
parent_page = StudiesIndexPage.objects.get(title="Study details")


# Gene details import
for index, row in f.iterrows():
    s = Studies()
    s.title = row["DOI"]
    s.doi = row["DOI"]
    s.papers = row["Papers"]
    s.study_population_description = row["Study_population_description"]
    s.unicef_regional_classification = row["UNICEF_regional_classification"]
    s.methods = row["Methods"]
    parent_page.add_child(instance=s)

# Gene details import
f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/gene_details.xlsx"
)
parent_page = GeneDetailsIndexPage.objects.get(title="Gene details")

f["RVIS_score"].where(f["RVIS_score"].notnull(), None)
f["RVIS_percentage"].where(f["RVIS_percentage"].notnull(), None)

for index, row in f.iterrows():
    s = GeneDetails()
    s.title = row["Gene"]
    s.gene = row["Gene"]
    s.cytoband_position = row["Cytoband_position"]
    s.omim = row["OMIM"]
    s.rvis_score = row["RVIS_score"]
    s.rvis_percentage = row["RVIS_percentage"]
    parent_page.add_child(instance=s)
