from django                    import forms
from .models                   import *        #Post, Usuario, Comment
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions    import ValidationError
	

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'titulo_post',
			'contenido',
			'categoria',]
		labels = {
			'titulo_post': 'Titulo',
			'contenido': 'Contenido',
			'categoria': 'Categoria',
		}
		widgets = {
			'titulo_post': forms.TextInput(attrs={'class':'form_control'}),
			'contenido': forms.Textarea(attrs={'class':'form_control', 'rows':5, 'placeholder':'Ingrese contenido del  post.'}),
			'categoria': forms.Select(),
		}

class UsuarioForm(UserCreationForm):
	username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Ingrese usuario'}))
	first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Ingrese nombre'}))
	last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Ingrese apellido'}))
	email = forms.CharField(label="E-mail", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":'Ingrese e-mail'}))
	# password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Usuario
		fields = ['username','first_name', 'last_name', 'email']
		# labels = {'username': 'Nombre de Usuario', 'titulo_post': 'Titulo','contenido': 'Contenido', 'categoria': 'Categoria'}
		# widgets = {'author': forms.TextInput(attrs={'class':'form_control'}),'titulo_post': forms.TextInput(attrs={'class':'form_control'}), 'contenido': forms.TextInput(attrs={'class':'form_control'}),'categoria': forms.CheckboxSelectMultiple()}
	"""
	def clean_username(self):
		username = self.cleaned_data["username"]
		if "123" in username:
			raise ValidationError("El nombre de usuario debe incluir la cadena 123") 
		return username
	"""


