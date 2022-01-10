from .models import VariantDetails
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

class VariantDetailsAdmin(ModelAdmin):
    model = VariantDetails
    menu_label = "Variant Details"
    menu_icon = "placeholder"
    menu_order = 700
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("variant_name",)
    search_fields = ("variant_name",)

modeladmin_register(VariantDetailsAdmin)
