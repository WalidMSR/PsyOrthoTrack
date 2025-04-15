from django import forms
from .models import Evaluation

class EvaluationDocumentForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'prenom': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'titre': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'description': forms.Select(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'score1': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'score2': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'score3':forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'score4':forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),

            }
