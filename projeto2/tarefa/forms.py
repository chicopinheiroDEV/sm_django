from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'concluido']
        labels = {
            'nome': 'Nome da Tarefa',
            'descricao': 'Descrição da Tarefa',
            'concluido': 'A tarefa está concluída? (sim/não)'
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 5:
            raise forms.ValidationError('O nome tem que ter no mínimo 5 caracteres')
        return nome
    
    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if descricao and len(descricao) < 10:
            raise forms.ValidationError('O nome tem que ter no mínimo 10 caracteres')
        return descricao