import json
import operator
from decimal import Decimal

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from numpy import full
from study_variants.models import StudyVariants


def operator_check(operator: str, filter_base: str, search_value: str) -> Q:
    """Implements Djangos double-underscore filters such as less-than-or-equal.

    Args:
        rule (dict): A dictionary entry representing an individual JQuery QueryBuilder rule.
        filter_base (str): A string representing the base Django model filter string to which we will add the appropriate logic filter.

    Returns:
        Q: A Q() object representation of the rule, complete with its appropriate logic.
    """

    base_dictionary = dict()
    if operator == "less":
        base_dictionary[filter_base + "__lt"] = search_value
        return Q(**base_dictionary)
    elif operator == "greater":
        base_dictionary[filter_base + "__gt"] = search_value
        return Q(**base_dictionary)
    elif operator == "less_or_equal":
        base_dictionary[filter_base + "__lte"] = search_value
        return Q(**base_dictionary)
    elif operator == "greater_or_equal":
        base_dictionary[filter_base + "__gte"] = search_value
        return Q(**base_dictionary)
    elif operator == "equal":
        base_dictionary[filter_base + "__icontains"] = search_value
        return Q(**base_dictionary)
    elif operator == "not_equal":
        base_dictionary[filter_base + "__icontains"] = search_value
        return ~Q(**base_dictionary)


def filter_type_to_q(rule: str) -> Q:
    """Check what type of filter it is and process to Q() object. (Calls another function for -> Q() conversion)

    Args:
        rule (dict): The individual JQuery QueryBuilder rule as a dictionary

    Returns:
        Q: A Django Q() object instance representing the JQuery QueryBuilder rule.
    """
    if rule["type"] == "integer":
        if rule["field"] == "RVIS":  # <Select> element
            filter_string_base = "variant__gene__rvis_score"
            return operator_check(rule["operator"], filter_string_base, 0)
        elif rule["field"] == "Odds ratio":  # <Select> element
            filter_string_base = "odds_ratio"
            return operator_check(rule["operator"], filter_string_base, rule["value"])
    elif rule["type"] == "double":
        if rule["field"] == "P-value":  # <Select> element
            filter_string_base = "p_value"
            return operator_check(rule["operator"], filter_string_base, rule["value"])
    elif rule["type"] == "string":
        if rule["field"] == "Condition":  # <Radio> element
            if rule["value"] == "CP":
                filter_string_base = "condition"
                return operator_check(
                    rule["operator"], filter_string_base, rule["value"]
                )
            elif rule["value"] == "NESHIE":
                filter_string_base = "condition"
                return operator_check(rule["operator"], filter_string_base, "HIE")
            elif rule["value"] == "NESHIE-caused CP":
                full_query = Q()
                condition_tup = [
                    ("condition_description", "HIE"),
                    ("condition_description", "Asphyxia"),
                    (
                        "condition_description",
                        "Neonatal encephalopathy",
                    ),
                ]
                for key, value in condition_tup:
                    q_object = operator_check(rule["operator"], key, value)
                    full_query.add(q_object, Q.OR)
                return full_query
        elif rule["field"] == "Gene HPO":  # <Text> element
            filter_string_base = "variant__gene__gene_hpo__name"
            return operator_check(rule["operator"], filter_string_base, rule["value"])
        elif rule["field"] == "Variant consequences":  # <Select> element
            filter_string_base = "variant__ensembl_vep__consequence_terms"
            return operator_check(rule["operator"], filter_string_base, rule["value"])
        elif rule["field"] == "Predicted variant effect":  # <Radio> element
            if rule["value"] == "Pathogenic":
                full_query = Q()
                path_effect_tup = [
                    ("variant__ensembl_vep__polyphen2_hvar_pred", "P"),
                    ("variant__ensembl_vep__sift_prediction", "pathogenic"),
                    ("variant__ensembl_vep__sift4g_pred", "P"),
                    ("variant__ensembl_vep__fathmm_pred", "P"),
                ]
                for key, value in path_effect_tup:
                    q_object = operator_check(rule["operator"], key, value)
                    full_query.add(q_object, Q.OR)
                return full_query
            elif rule["value"] == "Deleterious":
                full_query = Q()
                del_effect_tup = [
                    ("variant__mt_vep__query_prediction", "disease causing"),
                    ("variant__ensembl_vep__polyphen2_hvar_pred", "D"),
                    ("variant__ensembl_vep__sift_prediction", "deleterious"),
                    ("variant__ensembl_vep__sift4g_pred", "D"),
                    ("variant__ensembl_vep__fathmm_pred", "D"),
                ]
                for key, value in del_effect_tup:
                    q_object = operator_check(rule["operator"], key, value)
                    full_query.add(q_object, Q.OR)
                return full_query


def tree_explorer(data: dict) -> Q:
    """Generates a full Django Q() object with complex nested AND/OR logic.

    Args:
        data (dict): A python dictionary of the JQuery QueryBuilder JSON output.

    Returns:
        Q: A complex Django-compatible Q() object representing the complex query.

    Yields:
        Iterator[Q]: Q() instance generator for recursive parsing of nested complex queries.
    """
    # print(data)
    # print(type(data))
    if "type" in data:
        # Assume its a valid rule and yield into Q() representation:
        yield filter_type_to_q(data)
    elif "condition" in data:
        # Assume it is a nested group and call this generator recursively,
        # constructing this groups complex Q() object in the process:
        query = Q()
        for rule in data["rules"]:
            # Get next() result from generator above
            # (bc recursive yields) and process logic:
            for rule_instance in tree_explorer(rule):
                if data["condition"] == "AND":
                    query.add(rule_instance, Q.AND)
                if data["condition"] == "OR":
                    query.add(rule_instance, Q.OR)

        # Yield the completed, compiled logic for this branch
        # of query back up the pipe:
        yield query


def search(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page = request.GET.get("page", 1)

    # Filter_queries
    complex_filter_query = json.loads(request.GET.get("complex_filter_query", "{}"))

    search_query = request.GET.get("query", None)

    search_results = StudyVariants.objects.all()

    # Search
    if complex_filter_query is not None and "condition" in complex_filter_query:
        q_filter = next(tree_explorer(complex_filter_query))
        search_results = search_results.filter(q_filter)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "complex_filter_query": json.dumps(complex_filter_query)
            if complex_filter_query
            else json.dumps(dict()),
        },
    )
