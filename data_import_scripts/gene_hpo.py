import pandas as pd

f = pd.read_excel(
    "/usr/share/nginx/html/data_files/gene_hpo.xlsx"
)

f = f.astype(object).where(f.notnull(), None)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["InputTerm"])
    if a.exists():
        s = GeneHpo()
        s.symbol = row["Symbol"]
        s.inputterm = a[0]
        s.name = row["Name"]
        s.hpoid = row["HPOId"]
        s.alternativeid = row["AlternativeId"]
        s.definition = row["Definition"]
        s.save()
        # print(s)
    else:
        print("No corresponding gene name")
        print(row)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["InputTerm"])
    if a.exists():
        s = GeneHpo.objects.get(inputterm=a[0], name=row["Name"])
        s.symbol = row["Symbol"]
        s.save()
        # print(s)
    else:
        print("No corresponding gene name")
        print(row)

# Update entries

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/13122021_Online_DB_MAR.xlsx",
    sheet_name="Gene_HPO",
)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["InputTerm"])
    b = GeneHpo.objects.filter(symbol=row["Symbol"], name=row["Name"])
    if a.exists() and not b.exists():
        print("missing entry")
        s = GeneHpo()
        s.symbol = row["Symbol"]
        s.inputterm = a[0]
        s.name = row["Name"]
        s.hpoid = row["HPOId"]
        s.alternativeid = row["AlternativeId"]
        s.definition = row["Definition"]
        s.save()
        # print(s)
    else:
        print("Entry already exists")
