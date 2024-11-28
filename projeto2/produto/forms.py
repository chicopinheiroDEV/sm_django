from django import forms
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']
        labels = {
            'nome': 'Nome do produto',
            'preco': 'Preço do produto',
            'estoque': 'Estoque'
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError('O nome tem que ter no mínimo 3 caracteres')
        return nome