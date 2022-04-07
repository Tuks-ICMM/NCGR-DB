from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import EnsemblVep, MtVep, VariantDetails


class VariantDetailsAdmin(ModelAdmin):
    model = VariantDetails
    menu_label = "Variant Details"
    menu_icon = "edit"
    menu_order = 700
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("variant_name",)
    search_fields = ("variant_name",)


modeladmin_register(VariantDetailsAdmin)


# class EnsemblVepAdmin(ModelAdmin):
#     model = EnsemblVep
#     menu_label = "Ensembl VEP"
#     menu_icon = "edit"
#     menu_order = 800
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     list_display = ("variant",)
#     search_fields = ("variant",)


# modeladmin_register(EnsemblVepAdmin)


# class MtVepAdmin(ModelAdmin):
#     model = MtVep
#     menu_label = "Mutation Taster VEP"
#     menu_icon = "edit"
#     menu_order = 900
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     list_display = ("variant",)
#     search_fields = ("variant",)


# modeladmin_register(MtVepAdmin)
