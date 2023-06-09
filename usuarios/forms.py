from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            {'class': 'form-control',
             'placeholder': 'Ex.: João Silva'}
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite a sua senha'}
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            {'class': 'form-control',
             'placeholder': 'Ex.: João Silva'}
        )
    )
    email=forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            {'class': 'form-control',
             'placeholder': 'Ex.: joaosilva@xpto.com'}
        )
    )
    password1=forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            {'class': 'form-control',
             'placeholder': 'Digite sua senha'}
        )
    )
    password2=forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            {'class': 'form-control',
             'placeholder': 'Digite sua senha mais uma vez'}
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
     
     
    def clean_password2(self):
        senha1 = self.cleaned_data.get('password1')
        senha2 = self.cleaned_data.get('password2')

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('As senhas digitadas não conferem')
            else:
                return senha2
