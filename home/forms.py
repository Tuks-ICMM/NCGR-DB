from django import forms
import sys

sys.path.append(
    "C:/Users/Lance/Desktop/Megan/MSc_2/Online_db/neshiedbv7_links_working/mysite/study_variants"
)
import study_variants.models


class filter_form(forms.ModelForm):
    choices = study_variants.models.StudyVariants.objects.all()
    conditions = forms.ModelChoiceField(
        queryset=study_variants.models.StudyVariants.objects.all().distinct(),
    )

    class Meta:
        model = study_variants.models.StudyVariants
        fields = ("condition",)
