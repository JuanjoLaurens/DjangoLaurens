from django import forms
from .pqrsf import pqrsf
#Creamos las clases con los formularios

class ContactForm(forms.Form): 

    tipomsj = forms.ChoiceField(label="Tipo de petición", required = True, choices=pqrsf, widget=forms.Select(attrs={'class':'form-control'}))
    nombre = forms.CharField(label="Nombre ", required = True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nombre'}))
    apellido = forms.CharField(label="Apeliido ", required = True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu apellido'}))
    correo = forms.EmailField(label="Correo electronico", required = True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu correo'}))
    mensaje = forms.CharField(label="Mensaje", required = True, widget= forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tu mensaje'}))