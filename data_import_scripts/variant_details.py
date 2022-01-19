import pandas as pd

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/variant_details.xlsx"
)
parent_page = VariantDetailsIndexPage.objects.get(title="Gene details")

f = f.astype(object).where(f.notnull(), None)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["Gene"])
    if not a.exists():
        s = GeneDetails()
        s.title = row["Gene"]
        s.gene = row["Gene"]
        s.cytoband_position = row["Cytoband_position"]
        s.omim = row["OMIM"]
        s.rvis_score = row["RVIS_score"]
        s.rvis_percentage = row["RVIS_percentage"]
        parent_page.add_child(instance=s)
    else:
        print("Existing Entry")
