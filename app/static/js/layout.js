//alert('Hola mundo');

//EVENTO PARA VALIDAR NUMEROS EN FORMULARIOS
document.addEventListener('DOMContentLoaded', function() {
    // Obtenemos todos los campos de texto en el formulario
    var camposTexto = document.querySelectorAll('input[type="text"]');

    // Agregamos el evento input a cada campo de texto
    camposTexto.forEach(function(input) {
        input.addEventListener('input', function(event) {
            // Validamos si el valor ingresado es un número
            if (!/^\d*\.?\d*$/.test(input.value)) {
                // Si no es un número, eliminamos el último carácter
                input.value = input.value.slice(0, -1);
            }
        });
    });
});





