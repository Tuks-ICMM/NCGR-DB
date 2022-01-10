from .models import GeneDetails, GeneHpo
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


class GeneDetailsAdmin(ModelAdmin):
    model = GeneDetails
    menu_label = "Gene Details"
    menu_icon = "placeholder"
    menu_order = 800
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "gene",
        "omim",
    )
    search_fields = (
        "gene",
        "omim",
    )


modeladmin_register(GeneDetailsAdmin)


class GeneHpoAdmin(ModelAdmin):
    model = GeneHpo
    menu_label = "Gene Hpo"
    menu_icon = "placeholder"
    menu_order = 900
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "symbol",
        "name",
    )
    search_fields = (
        "symbol",
        "name",
    )


modeladmin_register(GeneHpoAdmin)
