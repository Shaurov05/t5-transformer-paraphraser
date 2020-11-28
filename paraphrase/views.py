from django.shortcuts import render
from .forms import ParaphraseForm
from .t5_paws_model import paraphrase_text

def index(request):
    data = {}
    form = ParaphraseForm()
    if request.method == "POST":
        form = ParaphraseForm(request.POST)
        if form.is_valid():
            text = str(form.cleaned_data['text'])
            paraphrased_text = paraphrase_text(text)
            print('=='*10)
            print(paraphrased_text)
        data['text'] = paraphrased_text
    return render(request, 'index.html', {'form': form, 'data': data})

