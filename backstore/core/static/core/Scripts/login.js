//Validación Formulario inicio sesión con JQUERY 

$(document).ready(function()
        {
            $("#error").hide();
            $("#formulario").submit(function()
            {
                var mensaje=""; 
                if($("#email").val().trim().length==0)
                {
                    mensaje="Ingresa un correo electronico valido, por favor";
                }
                if($('#password').val().trim().length<6 ||$('#password').val().trim().length>16){
                    
                    mensaje="Tu contraseña debe tener un minimo de 6 carácteres y un maximo de 16";
                }
                if(mensaje !="")
                {
                    $("#error").html(mensaje); 
                    $("#error").show(); 
                    event.preventDefault(); 
                }

            });
        });