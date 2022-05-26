import pandas as pd

f = pd.read_excel(
    "/usr/share/nginx/html/data_files/study_variants.xlsx",
    sheet_name="study_variants",
)

f = f.astype(object).where(f.notnull(), None)

for index, row in f.iterrows():
    a = Studies.objects.filter(title=row["DOI"])
    b = VariantDetails.objects.filter(title=row["Variant_name"])
    if a.exists() and b.exists():
        s = StudyVariants()
        s.paper = a[0]
        s.variant = b[0]
        s.reported_allele_or_genotype = row["Reported_allele_or_genotype"]
        s.condition = row["Condition"]
        s.condition_description = row["Condition_description"]
        s.disease_status = row["Disease_status"]
        s.odds_ratio = row["Odds_ratio"]
        s.p_value = row["P_value"]
        s.save()
        # print(s)
    else:
        print("No corresponding study or variant name")
        print(row)

# f["Odds_ratio"] = f["Odds_ratio"].apply(lambda x: None if x == "None" else x)
# f["P_value"] = f["P_value"].apply(lambda x: None if x == "None" else x)

for index, row in f.iterrows():
    a = Studies.objects.filter(title=row["DOI"])
    b = VariantDetails.objects.filter(title=row["Variant_name"])
    try:
        print("--------------------------------")
        print(index)
        print(type(row["Odds_ratio"]))
        print(type(row["P_value"]))
        print("--------------------------------")
        s = StudyVariants.objects.get(
            paper=a[0],
            variant=b[0],
            reported_allele_or_genotype=row["Reported_allele_or_genotype"],
            condition=row["Condition"],
            condition_description=row["Condition_description"],
            disease_status=row["Disease_status"],
        )
        s.odds_ratio = row["Odds_ratio"]
        s.p_value = row["P_value"]
        s.save()
    # print(s)
    except Exception as e:
        print("--------------------------------")
        print(e)
        print(index)
        print(row)
        print("--------------------------------")
else:
    print("No corresponding study or variant")
    print(row)

# Updating database with new entries with new excel spreadsheet

import pandas as pd

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/13122021_Online_DB_MAR.xlsx",
    sheet_name="Study_variants",
)

for index, row in f.iterrows():
    a = Studies.objects.filter(title=row["DOI"])
    b = VariantDetails.objects.filter(title=row["Variant_name"])
    try:
        c = StudyVariants.objects.get(
            paper=a.first(),
            variant=b.first(),
            reported_allele_or_genotype=row["Reported_allele_or_genotype"],
            condition=row["Condition"],
            condition_description=row["Condition_description"],
            disease_status=row["Disease_status"],
        )
    except Exception as e:
        print(e)

    if a.exists() and b.exists() and not c.exists():
        print("missing entry")
        s = StudyVariants()
        s.paper = a[0]
        s.variant = b[0]
        s.reported_allele_or_genotype = row["Reported_allele_or_genotype"]
        s.condition = row["Condition"]
        s.condition_description = row["Condition_description"]
        s.disease_status = row["Disease_status"]
        s.odds_ratio = row["Odds_ratio"]
        s.p_value = row["P_value"]
        s.save()
        print(s)
    else:
        print("No corresponding study or variant name")
        print(row)
