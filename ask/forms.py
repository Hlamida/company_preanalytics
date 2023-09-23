from django import forms

from .models import PredictModel


class PredictForm(forms.ModelForm):

    class Meta:
        model = PredictModel
        fields = '__all__'
        empty_label = None

    def __init__(self, *args, **kwargs):
        super(PredictForm, self).__init__(*args, **kwargs)
        self.fields[
            'base_okved'
        ].empty_label = None
        self.fields[
            'base_okved'
        ].widget.choices = self.fields['base_okved'].choices
