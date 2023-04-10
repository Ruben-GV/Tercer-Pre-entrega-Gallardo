from django import forms

class Profesorform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    apellido= forms.CharField(max_length=50, label="Apellidos")
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50, label="Profesión")

class Estudianteform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    apellido= forms.CharField(max_length=50, label="Apellidos")
    email= forms.EmailField()

class Cursoform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    comision= forms.CharField(max_length=50, label="Comisión")

class Entregableform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()