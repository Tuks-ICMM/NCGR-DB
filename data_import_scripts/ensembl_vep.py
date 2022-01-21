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
