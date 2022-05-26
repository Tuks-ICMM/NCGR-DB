import pandas as pd

f = pd.read_excel(
    "/usr/share/nginx/html/data_files/mt_vep.xlsx"
)

f = f.astype(object).where(f.notnull(), None)

for index, row in f.iterrows():
    a = VariantDetails.objects.filter(title=row["Variant_name"])
    if a.exists():
        s = MtVep()
        s.title = row["Variant_name"]
        s.variant = a[0]
        s.query_ncbi_geneid = row["Query_NCBI_geneid"]
        s.query_prediction = row["Query_prediction"]
        s.query_model = row["Query_model"]
        s.save()
        # print(s)
    else:
        print("No corresponding variant name")
        print(row)
