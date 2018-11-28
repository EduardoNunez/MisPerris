#Creamos este template para extender una clase, la cual seria el formulario
#para agregarle mas campos a pedir aparte del nombre de usuario y contraseña

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

# Importamos las excepciones.
from django.forms import ValidationError 

class CustomUserCreationForm(UserCreationForm): #Con esto estamos haciendo herencia y entendiendo la clase
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
     #El label lo usamos para ponerle nombre a lo que se va a mostrar al usuario
     #ya que si no lo colocamos se veria first_name
    last_name = forms.CharField(required=True, label="Apellido")

# ---------------------------------Validaciones---------------------------------
    # Validaremos que el email no existe para poder registrar.
    def clean_email(self):
        # Obtenemos el email que el usuario ingreso en el navegador.
        email = self.cleaned_data['email']

        usuario = User.objects.filter(email=email)

        if usuario:
            # Lanzamos una excepcion de validación.
            raise ValidationError("El email ya existe.")

    # Validaremos que el usuario no existe para poder registrar.
    # def clean_username(self):
        # Obtenemos el email que el usuario ingreso en el navegador.
        # username = self.cleaned_data['username']

        # usuario = User.objects.filter(username=username)

        # if usuario:
            # Lanzamos una excepcion de validación.
            # raise ValidationError("El usuario ya existe.")

# ------------------------------------------------------------------------------

    #Para que se guarde en la base de datos hay que hacer la siguien SubClase
    class Meta:
        #Le diremos al formulario que debe guardar los datos
        #utilizando el modelo User
        model = User
        #le diremos al formulario en que orden mostrar cada datos
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')