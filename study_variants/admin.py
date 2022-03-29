# Register your models here.
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import StudyVariants


class StudyVariantsAdmin(ModelAdmin):
    model = StudyVariants
    menu_label = "Study Variants"
    menu_icon = "placeholder"
    menu_order = 600
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("variant", "condition", "condition_description", "p_value")
    search_fields = ("variant", "condition", "condition_description", "p_value")


modeladmin_register(StudyVariantsAdmin)
