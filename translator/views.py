from django.shortcuts import render, redirect
from .forms import TranslationForm
from .models import Translation
from googletrans import Translator

def home(request):
    return redirect(translate_text)
def translate_text(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            source_language = form.cleaned_data['source_language']
            target_language = form.cleaned_data['target_language']
            source_text = form.cleaned_data['source_text']

            translator = Translator()
            translated_text = translator.translate(source_text, src=source_language, dest=target_language).text

            Translation.objects.create(
                source_language=source_language,
                target_language=target_language,
                source_text=source_text,
                translated_text=translated_text
            )

            return render(request, 'home.html', {'form': form, 'translated_text': translated_text})
    else:
        form = TranslationForm()

    return render(request, 'home.html', {'form': form})
