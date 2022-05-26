import pandas as pd
from os.path import join

f = pd.read_excel(
    "/usr/share/nginx/html/data_files/studies.xlsx"
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
