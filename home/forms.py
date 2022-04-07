import sys

import study_variants.models
from django import forms


class filter_form(forms.ModelForm):
    choices = study_variants.models.StudyVariants.objects.all()
    conditions = forms.ModelChoiceField(
        queryset=study_variants.models.StudyVariants.objects.all().distinct(),
    )

    class Meta:
        model = study_variants.models.StudyVariants
        fields = ("condition",)
