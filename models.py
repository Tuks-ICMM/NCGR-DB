# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnsemblVep(models.Model):
    variant = models.ForeignKey('VariantDetails', models.DO_NOTHING, db_column='Variant_id')  # Field name made lowercase.
    variant_name = models.TextField(db_column='Variant_name')  # Field name made lowercase.
    ensembl_canonical_hgvsc = models.TextField(db_column='Ensembl canonical HGVSC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consequence_terms = models.TextField(db_column='Consequence_terms', blank=True, null=True)  # Field name made lowercase.
    af_1000gp3_eur = models.DecimalField(db_column='AF_1000gp3_EUR', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    af_1000gp3 = models.DecimalField(db_column='AF_1000gp3', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    af_1000gp3_afr = models.DecimalField(db_column='AF_1000gp3_afr', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    af_1000gp3_amr = models.DecimalField(db_column='AF_1000gp3_amr', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    af_1000gp3_sas = models.DecimalField(db_column='AF_1000gp3_SAS', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    af_1000gp3_eas = models.DecimalField(db_column='AF_1000gp3_EAS', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    exac_adj_af = models.DecimalField(db_column='Exac_ADJ_AF', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    exac_afr_af = models.DecimalField(db_column='Exac_AFR_AF', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    exac_amr_af = models.DecimalField(db_column='Exac_AMR_AF', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    exac_eas_af = models.DecimalField(db_column='Exac_EAS_AF', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    exac_nfe_af = models.DecimalField(db_column='Exac_NFE_AF', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    exac_sas_af = models.DecimalField(db_column='Exac_SAS_AF', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    gnomad_genomes_af = models.DecimalField(db_column='GnomAD_genomes_af', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    gnomad_genomes_afr_af = models.DecimalField(db_column='GnomAD_genomes_afr_af', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    gnomad_genomes_eas_af = models.DecimalField(db_column='GnomAD_genomes_eas_af', max_digits=10, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    study_acmg = models.TextField(db_column='Study_ACMG', blank=True, null=True)  # Field name made lowercase.
    polyphen2_hvar_score = models.TextField(db_column='Polyphen2_hvar_score', blank=True, null=True)  # Field name made lowercase.
    polyphen2_hvar_pred = models.TextField(db_column='Polyphen2_hvar_pred', blank=True, null=True)  # Field name made lowercase.
    sift4g_score = models.TextField(db_column='Sift4G_score', blank=True, null=True)  # Field name made lowercase.
    sift4g_pred = models.TextField(db_column='Sift4G_pred', blank=True, null=True)  # Field name made lowercase.
    fathmm_score = models.TextField(db_column='Fathmm_score', blank=True, null=True)  # Field name made lowercase.
    fathmm_pred = models.TextField(db_column='Fathmm_pred', blank=True, null=True)  # Field name made lowercase.
    sift_score = models.DecimalField(db_column='Sift_score', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sift_prediction = models.TextField(db_column='Sift_prediction', blank=True, null=True)  # Field name made lowercase.
    cadd_raw = models.DecimalField(db_column='CADD_raw', max_digits=7, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    cadd_phred = models.DecimalField(db_column='CADD_phred', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ensembl_vep'


class GeneDetails(models.Model):
    gene = models.CharField(db_column='Gene', primary_key=True, max_length=150)  # Field name made lowercase.
    cytoband_position = models.TextField(db_column='Cytoband_position', blank=True, null=True)  # Field name made lowercase.
    omim = models.IntegerField(db_column='OMIM', blank=True, null=True)  # Field name made lowercase.
    rvis_score = models.DecimalField(db_column='RVIS_score', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rvis_percentage = models.DecimalField(db_column='RVIS_percentage', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    slug = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gene_details'


class GeneDetailsGenedetailsindexpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    intro = models.TextField()

    class Meta:
        managed = False
        db_table = 'gene_details_genedetailsindexpage'


class GeneHpo(models.Model):
    inputterm = models.ForeignKey(GeneDetails, models.DO_NOTHING, db_column='InputTerm', blank=True, null=True)  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    hpoid = models.TextField(db_column='HPOId', blank=True, null=True)  # Field name made lowercase.
    alternativeid = models.TextField(db_column='AlternativeId', blank=True, null=True)  # Field name made lowercase.
    definition = models.TextField(db_column='Definition', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gene_hpo'


class HomeHomepage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'home_homepage'


class MtVep(models.Model):
    variant = models.ForeignKey('VariantDetails', models.DO_NOTHING, db_column='Variant_id')  # Field name made lowercase.
    variant_name = models.TextField(db_column='Variant_name')  # Field name made lowercase.
    reference_genome = models.TextField(db_column='Reference_genome', blank=True, null=True)  # Field name made lowercase.
    chromosome = models.TextField(db_column='Chromosome', blank=True, null=True)  # Field name made lowercase.
    genomic_start_position = models.IntegerField(db_column='Genomic_start_position', blank=True, null=True)  # Field name made lowercase.
    genomic_end_position = models.IntegerField(db_column='Genomic_end_position', blank=True, null=True)  # Field name made lowercase.
    reference_allele = models.TextField(db_column='Reference_allele', blank=True, null=True)  # Field name made lowercase.
    alternate_allele = models.TextField(db_column='Alternate_allele', blank=True, null=True)  # Field name made lowercase.
    query_chr = models.TextField(db_column='Query_chr', blank=True, null=True)  # Field name made lowercase.
    query_genomic_start_pos = models.IntegerField(db_column='Query_genomic_start_pos', blank=True, null=True)  # Field name made lowercase.
    query_ref = models.TextField(db_column='Query_ref', blank=True, null=True)  # Field name made lowercase.
    query_alt = models.TextField(db_column='Query_alt', blank=True, null=True)  # Field name made lowercase.
    query_transcript_stable = models.TextField(db_column='Query_transcript_stable', blank=True, null=True)  # Field name made lowercase.
    query_ncbi_geneid = models.TextField(db_column='Query_NCBI_geneid', blank=True, null=True)  # Field name made lowercase.
    query_prediction = models.TextField(db_column='Query_prediction', blank=True, null=True)  # Field name made lowercase.
    query_model = models.TextField(db_column='Query_model', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mt_vep'


class Studies(models.Model):
    doi = models.TextField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    papers = models.TextField(db_column='Papers', blank=True, null=True)  # Field name made lowercase.
    study_population_description = models.TextField(db_column='Study_population_description', blank=True, null=True)  # Field name made lowercase.
    unicef_regional_classification = models.TextField(db_column='UNICEF_regional_classification', blank=True, null=True)  # Field name made lowercase.
    methods = models.TextField(db_column='Methods', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studies'


class StudyVariants(models.Model):
    paper = models.ForeignKey(Studies, models.CASCADE, db_column='Paper_id')  # Field name made lowercase.
    variant = models.ForeignKey('VariantDetails', models.CASCADE, db_column='Variant_id')  # Field name made lowercase.
    variant_name = models.TextField(db_column='Variant_name')  # Field name made lowercase.
    reported_allele_or_genotype = models.TextField(db_column='Reported_allele_or_genotype', blank=True, null=True)  # Field name made lowercase.
    condition = models.TextField(db_column='Condition', blank=True, null=True)  # Field name made lowercase.
    condition_description = models.TextField(db_column='Condition_description', blank=True, null=True)  # Field name made lowercase.
    disease_status = models.TextField(db_column='Disease_status', blank=True, null=True)  # Field name made lowercase.
    odds_ratio = models.DecimalField(db_column='Odds_ratio', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    p_value = models.DecimalField(db_column='P_value', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_variants'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class VariantDetails(models.Model):
    variant_name = models.CharField(db_column='Variant_name', max_length=150)  # Field name made lowercase.
    reference_genome = models.TextField(db_column='Reference_genome', blank=True, null=True)  # Field name made lowercase.
    transcript_id = models.TextField(db_column='Transcript_ID', blank=True, null=True)  # Field name made lowercase.
    chromosome = models.TextField(db_column='Chromosome', blank=True, null=True)  # Field name made lowercase.
    genomic_start_position = models.TextField(db_column='Genomic_start_position', blank=True, null=True)  # Field name made lowercase.
    genomic_end_position = models.TextField(db_column='Genomic_end_position', blank=True, null=True)  # Field name made lowercase.
    reference_allele = models.TextField(db_column='Reference_allele', blank=True, null=True)  # Field name made lowercase.
    alternate_allele = models.TextField(db_column='Alternate_allele', blank=True, null=True)  # Field name made lowercase.
    disease_association_with_ref_allele = models.TextField(db_column='Disease_association_with_ref_allele', blank=True, null=True)  # Field name made lowercase.
    variant_type = models.TextField(db_column='Variant_type', blank=True, null=True)  # Field name made lowercase.
    gene = models.ForeignKey(GeneDetails, models.DO_NOTHING, db_column='Gene')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variant_details'


class WagtailadminAdmin(models.Model):

    class Meta:
        managed = False
        db_table = 'wagtailadmin_admin'


class WagtailcoreCollection(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collection'


class WagtailcoreCollectionviewrestriction(models.Model):
    restriction_type = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collectionviewrestriction'


class WagtailcoreCollectionviewrestrictionGroups(models.Model):
    collectionviewrestriction = models.ForeignKey(WagtailcoreCollectionviewrestriction, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collectionviewrestriction_groups'
        unique_together = (('collectionviewrestriction', 'group'),)


class WagtailcoreComment(models.Model):
    text = models.TextField()
    contentpath = models.TextField()
    position = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    resolved_at = models.DateTimeField(blank=True, null=True)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)
    resolved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    revision_created = models.ForeignKey('WagtailcorePagerevision', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_comment'


class WagtailcoreCommentreply(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.ForeignKey(WagtailcoreComment, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_commentreply'


class WagtailcoreGroupapprovaltask(models.Model):
    task_ptr = models.OneToOneField('WagtailcoreTask', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupapprovaltask'


class WagtailcoreGroupapprovaltaskGroups(models.Model):
    groupapprovaltask = models.ForeignKey(WagtailcoreGroupapprovaltask, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupapprovaltask_groups'
        unique_together = (('groupapprovaltask', 'group'),)


class WagtailcoreGroupcollectionpermission(models.Model):
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupcollectionpermission'
        unique_together = (('group', 'collection', 'permission'),)


class WagtailcoreGrouppagepermission(models.Model):
    permission_type = models.CharField(max_length=20)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_grouppagepermission'
        unique_together = (('group', 'page', 'permission_type'),)


class WagtailcoreLocale(models.Model):
    language_code = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'wagtailcore_locale'


class WagtailcoreModellogentry(models.Model):
    label = models.TextField()
    action = models.CharField(max_length=255)
    data_json = models.TextField()
    timestamp = models.DateTimeField()
    content_changed = models.IntegerField()
    deleted = models.IntegerField()
    object_id = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_modellogentry'


class WagtailcorePage(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    live = models.IntegerField()
    has_unpublished_changes = models.IntegerField()
    url_path = models.TextField()
    seo_title = models.CharField(max_length=255)
    show_in_menus = models.IntegerField()
    search_description = models.TextField()
    go_live_at = models.DateTimeField(blank=True, null=True)
    expire_at = models.DateTimeField(blank=True, null=True)
    expired = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    locked = models.IntegerField()
    latest_revision_created_at = models.DateTimeField(blank=True, null=True)
    first_published_at = models.DateTimeField(blank=True, null=True)
    live_revision = models.ForeignKey('WagtailcorePagerevision', models.DO_NOTHING, blank=True, null=True)
    last_published_at = models.DateTimeField(blank=True, null=True)
    draft_title = models.CharField(max_length=255)
    locked_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    translation_key = models.CharField(max_length=32)
    locale = models.ForeignKey(WagtailcoreLocale, models.DO_NOTHING)
    alias_of = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_page'
        unique_together = (('translation_key', 'locale'),)


class WagtailcorePagelogentry(models.Model):
    label = models.TextField()
    action = models.CharField(max_length=255)
    data_json = models.TextField()
    timestamp = models.DateTimeField()
    content_changed = models.IntegerField()
    deleted = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    page_id = models.IntegerField()
    revision_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagelogentry'


class WagtailcorePagerevision(models.Model):
    submitted_for_moderation = models.IntegerField()
    created_at = models.DateTimeField()
    content_json = models.TextField()
    approved_go_live_at = models.DateTimeField(blank=True, null=True)
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagerevision'


class WagtailcorePagesubscription(models.Model):
    comment_notifications = models.IntegerField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagesubscription'
        unique_together = (('page', 'user'),)


class WagtailcorePageviewrestriction(models.Model):
    password = models.CharField(max_length=255)
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    restriction_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pageviewrestriction'


class WagtailcorePageviewrestrictionGroups(models.Model):
    pageviewrestriction = models.ForeignKey(WagtailcorePageviewrestriction, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pageviewrestriction_groups'
        unique_together = (('pageviewrestriction', 'group'),)


class WagtailcoreSite(models.Model):
    hostname = models.CharField(max_length=255)
    port = models.IntegerField()
    is_default_site = models.IntegerField()
    root_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    site_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailcore_site'
        unique_together = (('hostname', 'port'),)


class WagtailcoreTask(models.Model):
    name = models.CharField(max_length=255)
    active = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_task'


class WagtailcoreTaskstate(models.Model):
    status = models.CharField(max_length=50)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    page_revision = models.ForeignKey(WagtailcorePagerevision, models.DO_NOTHING)
    task = models.ForeignKey(WagtailcoreTask, models.DO_NOTHING)
    workflow_state = models.ForeignKey('WagtailcoreWorkflowstate', models.DO_NOTHING)
    finished_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_taskstate'


class WagtailcoreWorkflow(models.Model):
    name = models.CharField(max_length=255)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflow'


class WagtailcoreWorkflowpage(models.Model):
    page = models.OneToOneField(WagtailcorePage, models.DO_NOTHING, primary_key=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowpage'


class WagtailcoreWorkflowstate(models.Model):
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    current_task_state = models.OneToOneField(WagtailcoreTaskstate, models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    requested_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowstate'


class WagtailcoreWorkflowtask(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    task = models.ForeignKey(WagtailcoreTask, models.DO_NOTHING)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowtask'
        unique_together = (('workflow', 'task'),)


class WagtaildocsDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    file_hash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wagtaildocs_document'


class WagtaildocsUploadeddocument(models.Model):
    file = models.CharField(max_length=200)
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtaildocs_uploadeddocument'


class WagtailembedsEmbed(models.Model):
    url = models.TextField()
    max_width = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=10)
    html = models.TextField()
    title = models.TextField()
    author_name = models.TextField()
    provider_name = models.TextField()
    thumbnail_url = models.TextField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField()
    hash = models.CharField(unique=True, max_length=32)
    cache_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailembeds_embed'


class WagtailformsFormsubmission(models.Model):
    form_data = models.TextField()
    submit_time = models.DateTimeField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailforms_formsubmission'


class WagtailimagesImage(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField()
    focal_point_x = models.PositiveIntegerField(blank=True, null=True)
    focal_point_y = models.PositiveIntegerField(blank=True, null=True)
    focal_point_width = models.PositiveIntegerField(blank=True, null=True)
    focal_point_height = models.PositiveIntegerField(blank=True, null=True)
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    file_hash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wagtailimages_image'


class WagtailimagesRendition(models.Model):
    file = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    focal_point_key = models.CharField(max_length=16)
    filter_spec = models.CharField(max_length=255)
    image = models.ForeignKey(WagtailimagesImage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailimages_rendition'
        unique_together = (('image', 'filter_spec', 'focal_point_key'),)


class WagtailimagesUploadedimage(models.Model):
    file = models.CharField(max_length=200)
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailimages_uploadedimage'


class WagtailredirectsRedirect(models.Model):
    old_path = models.CharField(max_length=255)
    is_permanent = models.IntegerField()
    redirect_link = models.CharField(max_length=255)
    redirect_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(WagtailcoreSite, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailredirects_redirect'
        unique_together = (('old_path', 'site'),)


class WagtailsearchEditorspick(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    query = models.ForeignKey('WagtailsearchQuery', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_editorspick'


class WagtailsearchIndexentry(models.Model):
    object_id = models.CharField(max_length=50)
    title_norm = models.FloatField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    autocomplete = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry'
        unique_together = (('content_type', 'object_id'),)


class WagtailsearchQuery(models.Model):
    query_string = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_query'


class WagtailsearchQuerydailyhits(models.Model):
    date = models.DateField()
    hits = models.IntegerField()
    query = models.ForeignKey(WagtailsearchQuery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_querydailyhits'
        unique_together = (('query', 'date'),)


class WagtailusersUserprofile(models.Model):
    submitted_notifications = models.IntegerField()
    approved_notifications = models.IntegerField()
    rejected_notifications = models.IntegerField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    preferred_language = models.CharField(max_length=10)
    current_time_zone = models.CharField(max_length=40)
    avatar = models.CharField(max_length=100)
    updated_comments_notifications = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wagtailusers_userprofile'
