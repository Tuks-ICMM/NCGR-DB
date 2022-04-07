from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import GeneDetails, GeneHpo


class GeneDetailsAdmin(ModelAdmin):
    model = GeneDetails
    menu_label = "Gene Details"
    menu_icon = "edit"
    menu_order = 1000
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
    menu_label = "Gene HPO"
    menu_icon = "edit"
    menu_order = 1100
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
