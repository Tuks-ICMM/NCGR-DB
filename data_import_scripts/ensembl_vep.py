import pandas as pd

from variant_details.models import EnsemblVep

f = pd.read_excel(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/Data_import/ensembl_vep.xlsx"
)

f = f.astype(object).where(f.notnull(), None)

for index, row in f.iterrows():
    a = VariantDetails.objects.filter(title=row["Variant_name"])
    if a.exists():
        s = EnsemblVep()
        s.title = row["Variant_name"]
        s.variant = a[0]
        s.ensembl_canonical_hgvsc = row["Ensembl canonical HGVSC"]
        s.consequence_terms = row["Consequence_terms"]
        s.af_1000gp3_eur = row["AF_1000gp3_EUR"]
        s.af_1000gp3 = row["AF_1000gp3"]
        s.af_1000gp3_afr = row["AF_1000gp3_afr"]
        s.af_1000gp3_amr = row["AF_1000gp3_amr"]
        s.af_1000gp3_sas = row["AF_1000gp3_SAS"]
        s.af_1000gp3_eas = row["AF_1000gp3_EAS"]
        s.exac_adj_af = row["Exac_ADJ_AF"]
        s.exac_afr_af = row["Exac_AFR_AF"]
        s.exac_amr_af = row["Exac_AMR_AF"]
        s.exac_eas_af = row["Exac_EAS_AF"]
        s.exac_nfe_af = row["Exac_NFE_AF"]
        s.exac_sas_af = row["Exac_SAS_AF"]
        s.gnomad_genomes_af = row["GnomAD_genomes_af"]
        s.gnomad_genomes_afr_af = row["GnomAD_genomes_afr_af"]
        s.gnomad_genomes_eas_af = row["GnomAD_genomes_eas_af"]
        s.study_acmg = row["Study_ACMG"]
        s.polyphen2_hvar_score = row["Polyphen2_hvar_score"]
        s.polyphen2_hvar_pred = row["Polyphen2_hvar_pred"]
        s.sift4g_score = row["Sift4G_score"]
        s.sift4g_pred = row["Sift4G_pred"]
        s.fathmm_score = row["Fathmm_score"]
        s.fathmm_pred = row["Fathmm_pred"]
        s.sift_score = row["Sift_score"]
        s.sift_prediction = row["Sift_prediction"]
        s.cadd_raw = row["CADD_raw"]
        s.cadd_phred = row["CADD_phred"]
        s.save()
        # print(s)
    else:
        print("No corresponding gene name")
        print(row)

# Update entries

f["AF_1000gp3_EUR"] = f["AF_1000gp3_EUR"].apply(lambda x: None if x == "None" else x)
f["AF_1000gp3"] = f["AF_1000gp3"].apply(lambda x: None if x == "None" else x)
f["AF_1000gp3_afr"] = f["AF_1000gp3_afr"].apply(lambda x: None if x == "None" else x)
f["AF_1000gp3_amr"] = f["AF_1000gp3_amr"].apply(lambda x: None if x == "None" else x)
f["AF_1000gp3_SAS"] = f["AF_1000gp3_SAS"].apply(lambda x: None if x == "None" else x)
f["AF_1000gp3_EAS"] = f["AF_1000gp3_EAS"].apply(lambda x: None if x == "None" else x)
f["Exac_ADJ_AF"] = f["Exac_ADJ_AF"].apply(lambda x: None if x == "None" else x)
f["Exac_AFR_AF"] = f["Exac_AFR_AF"].apply(lambda x: None if x == "None" else x)
f["Exac_AMR_AF"] = f["Exac_AMR_AF"].apply(lambda x: None if x == "None" else x)
f["Exac_EAS_AF"] = f["Exac_EAS_AF"].apply(lambda x: None if x == "None" else x)
f["Exac_NFE_AF"] = f["Exac_NFE_AF"].apply(lambda x: None if x == "None" else x)
f["Exac_SAS_AF"] = f["Exac_SAS_AF"].apply(lambda x: None if x == "None" else x)
f["GnomAD_genomes_af"] = f["GnomAD_genomes_af"].apply(
    lambda x: None if x == "None" else x
)
f["GnomAD_genomes_afr_af"] = f["GnomAD_genomes_afr_af"].apply(
    lambda x: None if x == "None" else x
)
f["GnomAD_genomes_eas_af"] = f["GnomAD_genomes_eas_af"].apply(
    lambda x: None if x == "None" else x
)
f["Study_ACMG"] = f["Study_ACMG"].apply(lambda x: None if x == "None" else x)
f["Polyphen2_hvar_score"] = f["Polyphen2_hvar_score"].apply(
    lambda x: None if x == "None" else x
)
f["Polyphen2_hvar_pred"] = f["Polyphen2_hvar_pred"].apply(
    lambda x: None if x == "None" else x
)
f["Sift4G_score"] = f["Sift4G_score"].apply(lambda x: None if x == "None" else x)
f["Sift4G_pred"] = f["Sift4G_pred"].apply(lambda x: None if x == "None" else x)
f["Fathmm_score"] = f["Fathmm_score"].apply(lambda x: None if x == "None" else x)
f["Fathmm_pred"] = f["Fathmm_pred"].apply(lambda x: None if x == "None" else x)
f["Sift_score"] = f["Sift_score"].apply(lambda x: None if x == "None" else x)
f["Sift_prediction"] = f["Sift_prediction"].apply(lambda x: None if x == "None" else x)
f["CADD_raw"] = f["CADD_raw"].apply(lambda x: None if x == "None" else x)
f["CADD_phred"] = f["CADD_phred"].apply(lambda x: None if x == "None" else x)

for index, row in f.iterrows():
    a = VariantDetails.objects.filter(title=row["Variant_name"])
    try:
        print("--------------------------------")
        print(index)
        print("--------------------------------")
        s = EnsemblVep.objects.get(
            variant=a[0],
        )
        s.af_1000gp3_eur = row["AF_1000gp3_EUR"]
        s.af_1000gp3 = row["AF_1000gp3"]
        s.af_1000gp3_afr = row["AF_1000gp3_afr"]
        s.af_1000gp3_amr = row["AF_1000gp3_amr"]
        s.af_1000gp3_sas = row["AF_1000gp3_SAS"]
        s.af_1000gp3_eas = row["AF_1000gp3_EAS"]
        s.exac_adj_af = row["Exac_ADJ_AF"]
        s.exac_afr_af = row["Exac_AFR_AF"]
        s.exac_amr_af = row["Exac_AMR_AF"]
        s.exac_eas_af = row["Exac_EAS_AF"]
        s.exac_nfe_af = row["Exac_NFE_AF"]
        s.exac_sas_af = row["Exac_SAS_AF"]
        s.gnomad_genomes_af = row["GnomAD_genomes_af"]
        s.gnomad_genomes_afr_af = row["GnomAD_genomes_afr_af"]
        s.gnomad_genomes_eas_af = row["GnomAD_genomes_eas_af"]
        s.study_acmg = row["Study_ACMG"]
        s.polyphen2_hvar_score = row["Polyphen2_hvar_score"]
        s.polyphen2_hvar_pred = row["Polyphen2_hvar_pred"]
        s.sift4g_score = row["Sift4G_score"]
        s.sift4g_pred = row["Sift4G_pred"]
        s.fathmm_score = row["Fathmm_score"]
        s.fathmm_pred = row["Fathmm_pred"]
        s.sift_score = row["Sift_score"]
        s.sift_prediction = row["Sift_prediction"]
        s.cadd_raw = row["CADD_raw"]
        s.cadd_phred = row["CADD_phred"]
        s.save()
    # print(s)
    except Exception as e:
        print("--------------------------------")
        print(e)
        print(index)
        print(row)
        print("--------------------------------")
else:
    print("No corresponding variant")
    print(row)

for index, row in f.iterrows():
    a = VariantDetails.objects.filter(title=row["Variant_name"])
    try:
        print("--------------------------------")
        print(index)
        print("--------------------------------")
        s = EnsemblVep.objects.get(
            variant=a[0],
        )
        s.polyphen2_hvar_pred = row["Polyphen2_hvar_pred"]
    # print(s)
    except Exception as e:
        print("--------------------------------")
        print(e)
        print(index)
        print(row)
        print("--------------------------------")
else:
    print("No corresponding variant")
    print(row)
