from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Studies

# Register your models here.


class StudiesAdmin(ModelAdmin):
    model = Studies
    menu_label = "Studies"
    menu_icon = "edit"
    menu_order = 500
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("papers", "doi", "study_population_description")
    search_fields = ("papers", "doi", "study_population_description")


modeladmin_register(StudiesAdmin)
