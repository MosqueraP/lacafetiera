from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Aqui escriber tu nombre'}), min_length=5, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Aqui escriber tu email'}), min_length=5, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Aqui escriber tu mensaje'}), min_length=10, max_length=800)