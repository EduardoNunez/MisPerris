from django.shortcuts import render

#Con este import estamos trayendo el formulario
from .forms import CustomUserCreationForm

def register(request):

    variables = {

        'form':CustomUserCreationForm
    }

    if request.POST:
        #Le pasamos al formulario de registro todo lo que el usuario ingresó en el navegador
        form = CustomUserCreationForm(request.POST)
        
        #Preguntaremos si el formulario es valido
        if form.is_valid():
            #si es valido le diremos que guarde los datos en la BBDD
            form.save()
            variables['mensaje'] = "Usuario Registrado Con Éxito."
        else:
            variables['mensaje'] = "No Se Ha Logrado Registrar El Usuario."
            #Si hay errores de validacion debemos volver a enviar el formulario al template, ya que este
            #lleva consigo los mensajes de validacion
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)