from django.shortcuts import render

from ask.forms import PredictForm
from ai_models.load_model import local_model_predict


def index(request):
    template = 'ask/index.html'
    form = PredictForm(request.POST or None)
    if form.is_valid():
        predict_result = local_model_predict(
            year=form.cleaned_data['year'],
            base_okved=form.cleaned_data['base_okved'],
            nalog=form.cleaned_data['nalog'],
            okfs=form.cleaned_data['okfs'],
            okopf=form.cleaned_data['okopf'],
            smsp=form.cleaned_data['smsp'],
        )

        return render(
            request, template, {
                'form': form,
                'deal': predict_result,
            }
        )

    return render(request, template, {'form': form})
