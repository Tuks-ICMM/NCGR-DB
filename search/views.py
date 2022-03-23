import json
from decimal import Decimal

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from gene_details.models import GeneHpo
from study_variants.models import StudyVariants
from variant_details.models import VariantDetails
from wagtail.core.models import Page
from wagtail.search.models import Query


def generate_q(rule: dict) -> Q:
    """convert a string entry into a Q object
    Args:
        rule (dict): The individual JQuery QueryBuilder rule as a dictionary
    Returns:
        Q: A Django Q() object instance representing the JQuery QueryBuilder rule.
    """

    if rule["type"] == "integer":
        return rule["value"]  # Perform Q() object lookup here
    elif rule["type"] == "string":
        return rule["value"]  # Perform Q() object lookup here
    elif rule["type"] == "double":
        if rule["field"] == "P-value":
            if rule["operator"] == "less":
                return Q(study_variants__p_value__lt=rule["value"])
            elif rule["operator"] == "greater":
                return Q(study_variants__p_value__gt=rule["value"])
            elif rule["operator"] == "less or equal":
                return Q(study_variants__p_value__lte=rule["value"])
            elif rule["operator"] == "greater or equal":
                return Q(study_variants__p_value__gte=rule["value"])
            elif rule["operator"] == "equal":
                return Q(study_variants__p_value=rule["value"])
                # return rule["value"]  # Perform Q() object lookup here


def compile_filter(data: dict) -> Q:
    """Generates a full Django Q() object with complex nested AND/OR logic.
    Args:
        data (dict): A python dictionary of the JQuery QueryBuilder JSON output.
    Returns:
        Q: A complex Django-compatible Q() object representing the complex query.
    Yields:
        Iterator[Q]: Q() instance generator for recursive parsing of nested complex queries.
    """

    if "type" in data:
        # Assume its a valid rule and yield into Q() representation:
        yield generate_q(data)
    elif "condition" in data:
        # Assume it is a nested group and call this generator recursively,
        # constructing this groups complex Q() object in the process:
        query = Q()
        for rule in data["rules"]:
            # Get next() result from generator above
            # (bc recursive yields) and process logic:
            for rule_instance in compile_filter(rule):
                if data["condition"] == "AND":
                    query.add(rule_instance, Q.AND)
                if data["condition"] == "OR":
                    query.add(rule_instance, Q.OR)

        # Yield the completed, compiled logic for this branch
        # of query back up the pipe:
        yield query


def search(request):
    page = request.GET.get("page", 1)

    # Filters
    condition_filter = (
        StudyVariants.objects.all()
        .values_list("condition", flat=True)
        .distinct()
        .order_by("condition")
    )

    condition_description_filter = (
        StudyVariants.objects.all()
        .values_list("condition_description", flat=True)
        .distinct()
        .order_by("condition_description")
        .exclude(condition_description=None)
    )

    hpo_term_filter = list(
        GeneHpo.objects.all()
        .distinct()
        .order_by("name")
        .exclude(name=None)
        .values_list("name", flat=True)
    )

    # Filter_queries
    complex_filter_query = request.GET.get("complex_filter_query", None)
    # if request.GET.get("complex_filter_query")
    # else json.loads("{}"),
    print(complex_filter_query)

    search_query = request.GET.get("query", None)
    CP_query = request.GET.get("CP_query", None)
    NESHIE_query = request.GET.get("NESHIE_query", None)
    NESHIE_CP_query = request.GET.get("NESHIE_query", None)
    condition_description_query = request.GET.getlist(
        "condition_description_query", None
    )
    p_value_query = request.GET.get("p_value_query", None)
    odds_ratio_query = request.GET.get("odds_ratio_query", None)
    pathogenic_query = request.GET.get("pathogenic_query", None)
    deleterious_query = request.GET.get("deleterious_query", None)
    rvis_query = request.GET.get("rvis_query", None)
    hpo_query = request.GET.getlist("hpo_query", None)

    # Search
    if complex_filter_query is not None and "condition" in complex_filter_query:
        q_filter = compile_filter(complex_filter_query)
        print(q_filter)
        # if complex_filter_query["condition"] == "AND":
        #     filter_rules = list()
        #     for rule in complex_filter_query["rules"]:
        #         if rule["id"] == "Condition":
        #             if rule["operator"] == "equal":
        #                 if rule["value"] == "NESHIE":
        #                     filter_rules.append(
        #                         Q(study_variants__condition__contains="HIE")
        #                     )
        #                 elif rule["value"] == "NESHIE-caused CP":
        #                     filter_rules.append(
        #                         Q(study_variants__condition_description__contains="HIE")
        #                         | Q(
        #                             study_variants__condition_description__contains="Asphyxia"
        #                         )
        #                         | Q(
        #                             study_variants__condition_description__contains="Neonatal encephalopathy"
        #                         )
        #                     )
        #                 elif rule["value"] == "CP":
        #                     filter_rules.append(
        #                         Q(study_variants__condition__contains="CP")
        #                     )
        #             elif rule["operator"] == "not_equal":
        #                 if rule["value"] == "NESHIE":
        #                     filter_rules.append(
        #                         ~Q(study_variants__condition__contains="HIE")
        #                     )
        #                 elif rule["value"] == "NESHIE-caused CP":
        #                     filter_rules.append(
        #                         ~Q(
        #                             study_variants__condition_description__contains="HIE"
        #                         )
        #                         | ~Q(
        #                             study_variants__condition_description__contains="Asphyxia"
        #                         )
        #                         | ~Q(
        #                             study_variants__condition_description__contains="Neonatal encephalopathy"
        #                         )
        #                     )
        #                 elif rule["value"] == "CP":
        #                     filter_rules.append(
        #                         ~Q(study_variants__condition__contains="CP")
        #                     )

        #         elif rule["id"] == "P-value":
        #             if rule["operator"] == "less":
        #                 filter_rules.append(
        #                     Q(study_variants__p_value__lt=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "greater":
        #                 filter_rules.append(
        #                     Q(study_variants__p_value__gt=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "less or equal":
        #                 filter_rules.append(
        #                     Q(study_variants__p_value__lte=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "greater or equal":
        #                 filter_rules.append(
        #                     Q(study_variants__p_value__gte=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "equal":
        #                 filter_rules.append(
        #                     Q(study_variants__p_value=Decimal(rule["value"]))
        #                 )

        #         elif rule["id"] == "Odds ratio":
        #             if rule["operator"] == "less":
        #                 filter_rules.append(
        #                     Q(study_variants__odds_ratio__lt=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "greater":
        #                 filter_rules.append(
        #                     Q(study_variants__odds_ratio__gt=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "less or equal":
        #                 filter_rules.append(
        #                     Q(study_variants__odds_ratio__lte=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "greater or equal":
        #                 filter_rules.append(
        #                     Q(study_variants__odds_ratio__lte=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "equal":
        #                 filter_rules.append(
        #                     Q(study_variants__odds_ratio=Decimal(rule["value"]))
        #                 )

        #         elif rule["id"] == "Predicted variant effect":
        #             if rule["operator"] == "equal":
        #                 if rule["value"] == "Pathogenic":
        #                     filter_rules.append(
        #                         Q(ensembl_vep__polyphen2_hvar_pred__contains="P")
        #                         | Q(ensembl_vep__sift_prediction__contains="pathogenic")
        #                         | Q(ensembl_vep__sift4g_pred__contains="P")
        #                         | Q(ensembl_vep__fathmm_pred__contains="P")
        #                     )
        #                 elif rule["value"] == "Deleterious":
        #                     filter_rules.append(
        #                         Q(mt_vep__query_prediction="disease causing")
        #                         | Q(
        #                             mt_vep__query_prediction="disease causing automatic"
        #                         )
        #                         | Q(ensembl_vep__polyphen2_hvar_pred__contains="D")
        #                         | Q(
        #                             ensembl_vep__sift_prediction__contains="deleterious"
        #                         )
        #                         | Q(ensembl_vep__sift4g_pred__contains="D")
        #                         | Q(ensembl_vep__fathmm_pred__contains="D")
        #                     )
        #             elif rule["operator"] == "not_equal":
        #                 if rule["value"] == "Pathogenic":
        #                     filter_rules.append(
        #                         ~Q(ensembl_vep__polyphen2_hvar_pred__contains="P")
        #                         | ~Q(
        #                             ensembl_vep__sift_prediction__contains="pathogenic"
        #                         )
        #                         | ~Q(ensembl_vep__sift4g_pred__contains="P")
        #                         | ~Q(ensembl_vep__fathmm_pred__contains="P")
        #                     )
        #                 elif rule["value"] == "Deleterious":
        #                     filter_rules.append(
        #                         ~Q(mt_vep__query_prediction="disease causing")
        #                         | ~Q(
        #                             mt_vep__query_prediction="disease causing automatic"
        #                         )
        #                         | ~Q(ensembl_vep__polyphen2_hvar_pred__contains="D")
        #                         | ~Q(
        #                             ensembl_vep__sift_prediction__contains="deleterious"
        #                         )
        #                         | ~Q(ensembl_vep__sift4g_pred__contains="D")
        #                         | ~Q(ensembl_vep__fathmm_pred__contains="D")
        #                     )

        #         elif rule["id"] == "RVIS":
        #             if rule["operator"] == "less":
        #                 filter_rules.append(
        #                     Q(gene__rvis_score__lt=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "less_or_equal":
        #                 filter_rules.append(
        #                     Q(gene__rvis_score__lte=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "greater":
        #                 filter_rules.append(
        #                     Q(gene__rvis_score__gt=Decimal(rule["value"]))
        #                 )
        #             elif rule["operator"] == "greater_or_equal":
        #                 filter_rules.append(
        #                     Q(gene__rvis_score__gte=Decimal(rule["value"]))
        #                 )
        #         elif rule["id"] == "Gene HPO":
        #             if rule["operator"] == "contains":
        #                 filter_rules.append(
        #                     Q(gene__gene_hpo__contains=str(rule["input"]))
        #                 )
        #             elif rule["operator"] == "equal":
        #                 filter_rules.append(Q(gene__gene_hpo=str(rule["input"])))
        #             elif rule["operator"] == "not_equal":
        #                 filter_rules.append(
        #                     ~Q(gene__gene_hpo__contains=str(rule["input"]))
        #                 )

        #         elif rule["id"] == "Variant consequences":
        #             if rule["operator"] == "equal":
        #                 filter_rules.append(
        #                     Q(ensembl_vep__consequence_terms__contains=rule["value"])
        #                 )
        #             if rule["operator"] == "not_equal":
        #                 filter_rules.append(
        #                     ~Q(ensembl_vep__consequence_terms__contains=rule["value"])
        #                 )

    # search_results = VariantDetails.objects.live()
    # if NESHIE_CP_query and NESHIE_query and CP_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition_description__contains="HIE")
    #         | Q(study_variants__condition_description__contains="Asphyxia")
    #         | Q(
    #             study_variants__condition_description__contains="Neonatal encephalopathy"
    #         )
    #         | Q(study_variants__condition__contains="HIE")
    #         | Q(study_variants__condition__contains="CP")
    #     )
    # elif NESHIE_CP_query and NESHIE_query and not CP_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition_description__contains="HIE")
    #         | Q(study_variants__condition_description__contains="Asphyxia")
    #         | Q(
    #             study_variants__condition_description__contains="Neonatal encephalopathy"
    #         )
    #         | Q(study_variants__condition__contains="HIE")
    #     )
    # elif NESHIE_CP_query and CP_query and not NESHIE_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition_description__contains="HIE")
    #         | Q(study_variants__condition_description__contains="Asphyxia")
    #         | Q(
    #             study_variants__condition_description__contains="Neonatal encephalopathy"
    #         )
    #         | Q(study_variants__condition__contains="CP")
    #     )
    # elif NESHIE_query and CP_query and not NESHIE_CP_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition__contains="HIE")
    #         | Q(study_variants__condition__contains="CP")
    #     )
    # elif NESHIE_CP_query and not CP_query and not NESHIE_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition_description__contains="HIE")
    #         | Q(study_variants__condition_description__contains="Asphyxia")
    #         | Q(
    #             study_variants__condition_description__contains="Neonatal encephalopathy"
    #         )
    #     )
    # elif NESHIE_query and not CP_query and not NESHIE_CP_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition__contains="HIE")
    #     )
    # elif CP_query and not NESHIE_query and not NESHIE_CP_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__condition__contains="CP")
    #     )
    # if p_value_query and odds_ratio_query:
    #     search_results = search_results.filter(
    #         Q(study_variants__p_value__lt=Decimal("0.05"))
    #         | Q(study_variants__odds_ratio__gt=Decimal("1"))
    #     )

    # elif p_value_query and not odds_ratio_query:
    #     search_results = search_results.filter(
    #         study_variants__p_value__lt=Decimal("0.05")
    #     )
    # elif odds_ratio_query and not p_value_query:
    #     search_results = search_results.filter(
    #         study_variants__odds_ratio__gt=Decimal("1")
    #     )

    # if pathogenic_query and deleterious_query:
    #     search_results = search_results.filter(
    #         Q(ensembl_vep__polyphen2_hvar_pred__contains="P")
    #         | Q(ensembl_vep__sift_prediction__contains="pathogenic")
    #         | Q(ensembl_vep__sift4g_pred__contains="P")
    #         | Q(ensembl_vep__fathmm_pred__contains="P")
    #         | Q(ensembl_vep__polyphen2_hvar_pred__contains="D")
    #         | Q(ensembl_vep__sift_prediction__contains="deleterious")
    #         | Q(ensembl_vep__sift4g_pred__contains="D")
    #         | Q(ensembl_vep__fathmm_pred__contains="D")
    #         | Q(mt_vep__query_prediction="disease causing")
    #         | Q(mt_vep__query_prediction="disease causing automatic")
    #     )

    # elif pathogenic_query and not deleterious_query:
    #     search_results = search_results.filter(
    #         Q(ensembl_vep__polyphen2_hvar_pred__contains="P")
    #         | Q(ensembl_vep__sift_prediction__contains="pathogenic")
    #         | Q(ensembl_vep__sift4g_pred__contains="P")
    #         | Q(ensembl_vep__fathmm_pred__contains="P")
    #     )
    # elif deleterious_query and not pathogenic_query:
    #     search_results = search_results.filter(
    #         Q(mt_vep__query_prediction="disease causing")
    #         | Q(mt_vep__query_prediction="disease causing automatic")
    #         | Q(ensembl_vep__polyphen2_hvar_pred__contains="D")
    #         | Q(ensembl_vep__sift_prediction__contains="deleterious")
    #         | Q(ensembl_vep__sift4g_pred__contains="D")
    #         | Q(ensembl_vep__fathmm_pred__contains="D")
    #     )
    # if rvis_query:
    #     search_results = search_results.filter(gene__rvis_score__lt=Decimal("0"))
    # # Change to elastic search
    # if condition_description_query:
    #     search_results = search_results.filter(
    #         study_variants__condition_description__in=condition_description_query
    #     )
    # if hpo_query:
    #     search_results = search_results.filter(gene__gene_hpo__name__in=hpo_query)

    # Pagination
    paginator = Paginator(search_results, 200)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "condition_filter": condition_filter,
            "condition_description_filter": condition_description_filter,
            "hpo_term_filter": hpo_term_filter,
            "condition_description_query": condition_description_query,
            "p_value_query": p_value_query,
            "odds_ratio_query": odds_ratio_query,
            "pathogenic_query": pathogenic_query,
            "deleterious_query": deleterious_query,
            "rvis_query": rvis_query,
            "hpo_query": hpo_query,
            "NESHIE_query": NESHIE_query,
            "NESHIE_CP_query": NESHIE_CP_query,
            "CP_query": CP_query,
            "complex_filter_query": json.dumps(complex_filter_query)
            if complex_filter_query
            else json.dumps(dict()),
        },
    )
