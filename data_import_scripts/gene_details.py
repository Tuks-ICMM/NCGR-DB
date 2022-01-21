import pandas as pd

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/gene_details.xlsx"
)
parent_page = GeneDetailsIndexPage.objects.get(title="Gene details")

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

f["RVIS_percentage"] = f["RVIS_percentage"].apply(
    lambda x: str(x) if not None else None
)
f["RVIS_score"] = f["RVIS_score"].apply(lambda x: str(x) if not None else None)

f["RVIS_percentage"] = f["RVIS_percentage"].apply(lambda x: None if x == "None" else x)

f["RVIS_score"] = f["RVIS_score"].apply(lambda x: None if x == "None" else x)

for index, row in f.iterrows():
    try:
        print("--------------------------------")
        print(index)
        print(type(row["RVIS_score"]))
        print(type(row["RVIS_percentage"]))
        print("--------------------------------")
        s = GeneDetails.objects.get(title=row["Gene"])
        s.rvis_score = row["RVIS_score"]
        s.rvis_percentage = row["RVIS_percentage"]
        s.save_revision().publish()
    # print(s)
    except Exception as e:
        print("--------------------------------")
        print(e)
        print(index)
        print(row)
        print("--------------------------------")
else:
    print("No corresponding gene name")
    print(row)
