$(document).ready(function() {
    $("#mascotaFormulario").validate({
        rules: {
            txtMascota: {
                required:true, /*Que sea "True" significa que es un campo obligatorio */
                minlength:3, /*Este indica el largo minimo*/
                maxlength:20 /*Este es el largo maximo*/
            },
            cboRaza:{
                required:true,
            },
            cboGenero:{
                required:true,
            },
            fechaIngreso:{
                required:true, 
                date:true,
            },
            fechaNacimiento:{
                required:false,
                date:true
            },
            imagen:{
                required:true
            },
            cboEstado:{
                required:true,
            }
            
        },messages: {
            txtMascota:{
                required:"Campo requerido",
                minlength:"Debe Ingresar mas largo",
                maxlength:"El nombre es demaciado largo"
            },
            cboRaza: {
                required:"Debe seleccionar una raza"
            },
            cboGenero: {
                required:"Le falta ingresar el genero"
            },
            fechaIngreso:{ 
                required:"Este campo es requerido"
            },
            imagen:{ 
                required:"Debe subir una foto !"
            },
            cboEstado: {
                required:"Debe seleccionar un estado"
            }
        }
    });
});
