import pandas as pd

from study_variants.models import StudyVariants

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/study_variants.xlsx",
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
