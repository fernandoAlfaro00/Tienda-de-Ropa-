$("#formulario").validate(
    {
        rules:{
            "rut":{
                required:true,
                minlength:5
            },
            "txtnombre":{
                required:true,
                accept: "[a-zA-Z]+",
                maxlength:40
            },
            "txtapellido":{
                required:true,
                accept: "[a-zA-Z]+",
                maxlength:40
            },
            "txtemail":{
                required:true,
                email:true
            },
            "txttelefono":{
                required:true,
                number:true,
                
                
            },
            "txtfecha_nac":{
                required:true
                
                
            },
            "txtregion":{
                required:true
            },
            "txtcomuna":{
                required:true
            },
            "txtvivienda":{
                required:true
            }
            
            
        },
        messages:{
            "rut":{
                required:"Ingrese un rut",
                minlength:"por favor ingrese mas de 5 caracteres"
            },
            "txtnombre":{
                required:"Ingrese un nombre",
                accept: "El Campo nombre Permite solo letras",            
                maxlength:"El campo Nombre No puede Tener mas de 30 caracteres"
                
            },
            "txtapellido":{
                required:"Ingrese un apellido",
                minlength:"El campo Nombre No puede Tener mas de 30 caracteres",
                accept: "El Campo apellido Permite solo letras"

            },
            "txtemail":{
                required:"Ingrese un Email",
                email:"Revise Email que Tenga un Formato Correcto ,Ej: adam.ses@gmail.com"
            },
            "txttelefono":{
                required:"Ingrese Un  numero de telefono",
                number:"Ingrese numero Valido"
            },
            "txtfecha_nac":{
                required:"Ingrese la Fecha de Nacimiento"
            },
            "txtregion":{
                required:"Seleccione una Region"
            },
            "txtcomuna":{
                required:"Seleccione una Comuna"
            },
            "txtvivienda":{
                required:"Seleccione una Vivienda"
            }
            

        }
    }
);

jQuery.validator.addMethod("accept", function(value, element, param) {
    return value.match(new RegExp("." + param + "$"));
  });