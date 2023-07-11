from django import forms

from apps.core.models import RequestCall


class RequestCallModelForm(forms.ModelForm):
    class Meta:
        model = RequestCall
        fields = '__all__'
        # exclude = ''
