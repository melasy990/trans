from django import forms
langs = [
    ('arabic', 'Arabic'),
    ('english', 'English'),
    ('russian', 'Russian'),
    ('spanish', 'Spanish'),
    ('fr', 'Frensh'),
    ('german', 'German'),
    ('japanese', 'Japanese'),
]
class TranslationForm(forms.Form):
    source_language = forms.ChoiceField(choices=langs)
    target_language = forms.ChoiceField(choices=langs)
    source_text = forms.CharField(widget=forms.Textarea)
