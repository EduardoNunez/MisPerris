$(document).ready(function() {
    $("#clienteFormulario").validate({
        rules: {
            txtCorreo: {
                required:true,
                email: true
            },
            txtRun: {
                required:true,
                minlength:11,
                maxlength:12
            },
            txtNombre: {
                required:true,
                minlength:8,
                maxlength:45
            },
            cboRegion: {
                required:true
            },
            cboCiudad: {
                required:true
            },
            cboTipoViv:{
                required:true
            },
            txtDireccion: {
                required:true,
                minlength:3,
                maxlength:150
            },
            fecha: {
                required:true,
                date:true,
                max:"2001-00-00",
            },
            txtTelefono: {
                required:true,
                min:10000000,
                max:99999999
            }
        },messages: {
            txtNombre:{
                required:"Campo requerido",
                minlength:"Debe Ingresar su nombre completo",
                maxlength:"El nombre es demaciado largo"
            },
            cboMarca: {
                required:"Eliga una opción"
            },
            txtTelefono:{ 
                required:"Este campo es requerido",
                min:"Ingrese los 8 ultimos digitos (ej:12345678)",
                max:"Ingrese los 8 ultimos digitos (ej:12345678)"
            },
            fecha:{ 
                required:"Este campo es requerido",
                max:"La fecha de nacimiento debe ser inferior a 2001"
            },txtRun:{ 
                required:"Este campo es requerido",
                minlength:"El rut es demaciado corto",
                maxlength:"no puede pasar de 12 caracteres"
            }
        }
    });
});







