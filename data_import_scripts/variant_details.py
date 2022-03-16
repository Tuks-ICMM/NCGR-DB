import pandas as pd

from gene_details.models import GeneDetails
from variant_details.models import VariantDetails

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/variant_details.xlsx"
)
parent_page = VariantDetailsIndexPage.objects.get(title="Variant details")

f = f.astype(object).where(f.notnull(), None)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["Gene"])
    if a.exists():
        s = VariantDetails()
        s.title = row["Variant_name"]
        s.gene = a[0]
        s.variant_name = row["Variant_name"]
        s.reference_genome = row["Reference_genome"]
        s.transcript_id = row["Transcript_ID"]
        s.chromosome = row["Chromosome"]
        s.genomic_start_position = row["Genomic_start_position"]
        s.genomic_end_position = row["Genomic_end_position"]
        s.reference_allele = row["Reference_allele"]
        s.alternate_allele = row["Alternate_allele"]
        s.disease_association_with_ref_allele = row[
            "Disease_association_with_ref_allele"
        ]
        s.variant_type = row["Variant_type"]
        parent_page.add_child(instance=s)
        # print(s)
    else:
        print("No corresponding gene name")
        print(row)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["Gene"])
    if a.exists():
        s = VariantDetails.objects.get(title=row["Variant_name"])
        s.chromosome = row["Chromosome"]
        s.save()
        # print(s)
    else:
        print("No corresponding gene name")
        print(row)

for item in VariantDetails.objects.all():
    item.disease_association_with_ref_allele = None
    item.save_revision().publish()

f = (
    f.astype(object)
    .where(f.notnull(), None).astype(bool))
    # .where(f["Disease_association_with_ref_allele"] == 0.0, False)
    # .where(f["Disease_association_with_ref_allele"] == 1.0, True)
) 

f.loc[:,"Disease_association_with_ref_allele"] = f.loc[:,"Disease_association_with_ref_allele"].astype(bool)

# Update existing database entries
for index, row in f.iterrows():
    a = VariantDetails.objects.filter(title=row["Variant_name"])
    if a.exists():
        s = VariantDetails.objects.get(title=row["Variant_name"])
        s.disease_association_with_ref_allele = row[
            "Disease_association_with_ref_allele"
        ]
        s.save_revision().publish()
        # print(s)
    else:
        print("No corresponding gene name")
        print(row)

# Updating database with new entries with new excel spreadsheet

import pandas as pd

parent_page = VariantDetailsIndexPage.objects.get(title="Variant details")

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/13122021_Online_DB_MAR.xlsx", sheet_name='Variant_details'
)

for index, row in f.iterrows():
    a = GeneDetails.objects.filter(title=row["Gene"])
    b = VariantDetails.objects.filter(title=row["Variant_name"])
    if a.exists() and not b.exists():
        print ("missing entry")
        s = VariantDetails()
        s.title = row["Variant_name"]
        s.gene = a[0]
        s.variant_name = row["Variant_name"]
        s.reference_genome = row["Reference_genome"]
        s.transcript_id = row["Transcript_ID"]
        s.chromosome = row["Chromosome"]
        s.genomic_start_position = row["Genomic_start_position"]
        s.genomic_end_position = row["Genomic_end_position"]
        s.reference_allele = row["Reference_allele"]
        s.alternate_allele = row["Alternate_allele"]
        s.disease_association_with_ref_allele = row[
            "Disease_association_with_ref_allele"
        ]
        s.variant_type = row["Variant_type"]
        parent_page.add_child(instance=s)
        print(s)
    else:
        print("Entry already exists")
        print(row)

