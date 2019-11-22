{
  $("#personForm").validate({
    rules: {
      run: {
        required: true,
        minlength: 5
      },
      first_name: {
        required: true,
        accept: "[a-zA-Z]+",
        maxlength: 40
      },
      last_name: {
        required: true,
        accept: "[a-zA-Z]+",
        maxlength: 40
      },
      email: {
        required: true,
        email: true
      },
      telefono: {
        required: true
      },
      fecha_nacimiento: {
        required: true
      },
      region: {
        required: true
      },
      comuna: {
        required: false
      },
      vivienda: {
        required: true
      }
    },
    messages: {
      run: {
        required: "Ingrese un rut",
        minlength: "por favor ingrese mas de 5 caracteres"
      },
      first_name: {
        required: "Ingrese un nombre",
        accept: "El Campo nombre Permite solo letras",
        maxlength: "El campo Nombre No puede Tener mas de 30 caracteres"
      },
      last_name: {
        required: "Ingrese un apellido",
        minlength: "El campo Nombre No puede Tener mas de 30 caracteres",
        accept: "El Campo apellido Permite solo letras"
      },
      email: {
        required: "Ingrese un Email",
        email:
          "Revise Email que Tenga un Formato Correcto ,Ej: adam.ses@gmail.com"
      },
      telefono: {
        required: "Ingrese Un  numero de telefono"
      },
      fecha_nacimiento: {
        required: "Ingrese la Fecha de Nacimiento"
      },
      region: {
        required: "Seleccione una Region"
      },
      comuna: {
        required: "Seleccione una Comuna"
      },
      vivienda: {
        required: "Seleccione una Vivienda"
      }
    }
  });

  jQuery.validator.addMethod("accept", function (value, element, param) {
    return value.match(new RegExp("." + param + "$"));
  });
}
