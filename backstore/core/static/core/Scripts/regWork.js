//Validación formulario de registro de trabajo con JQuery

$(document).ready(function()
        {
            $("#error").hide();
            $("#formulario").submit(function()
            {
                var mensaje=""; 
                var msjgood="Te contactaremos lo mas pronto posible :), gracias por tu interés!";

                if($("#nombre").val().trim().length==0)
                { 
                    mensaje="Ingresa un nombre valido, por favor";
                }
                if($("#apellido").val().trim().length==0)
                { 
                    mensaje="Ingresa un apellido valido, por favor";
                }

                if($("#email").val().trim().length==0)
                {
                    mensaje="Ingresa un correo electronico valido, por favor";
                }
                if($("#ciudad").val().trim().length==0)
                { 
                    mensaje="El campo ciudad está vacío";
                }
                if($("#telefono").val().trim().length<8)
                {
                    mensaje="Ingresa un número de telefono valido"
                }
                if($("#comentarios").val().trim().length<10)
                {
                    mensaje="Los comentarios deben tener mas de 10 caracteres"
                }
                if(mensaje !="")
                {
                    $("#error").html(mensaje); 
                    $("#error").show(); 
                    event.preventDefault(); 
                }

            });
        });