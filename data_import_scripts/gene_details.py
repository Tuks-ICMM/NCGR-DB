import pandas as pd

f = pd.read_excel(
    "/usr/share/nginx/html/data_files/gene_details.xlsx"
)
parent_page = GeneDetailsIndexPage.objects.get(title="Gene details")

f = f.astype(object).where(f.notnull(), None)
# f["RVIS_score"] = pd.to_numeric(f["RVIS_score"])
# f["RVIS_percentage"] = pd.to_numeric(f["RVIS_percentage"])

f["RVIS_percentage"] = f["RVIS_percentage"].apply(
    lambda x: str(x) if not None else None
)
f["RVIS_score"] = f["RVIS_score"].apply(lambda x: str(x) if not None else None)

f["RVIS_percentage"] = f["RVIS_percentage"].apply(lambda x: None if x == "None" else x)
f["RVIS_score"] = f["RVIS_score"].apply(lambda x: None if x == "None" else x)


for index, row in f.iterrows():
    try:
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
            print("----------------------")
            # print(s)
            # print(s.rvis_score)
            # print(type(s.rvis_score))
            # print(Decimal.from_float(s.rvis_score).quantize(TWO_PLACES))
            # print(type(Decimal.from_float(s.rvis_score).quantize(TWO_PLACES)))
            # print("----------------------")
        else:
            print("Existing Entry")
    except Exception as e:
        print("Exception: ", e)
