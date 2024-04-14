// Obtener una referencia al elemento canvas del DOM
const $grafica = document.querySelector("#grafica");

// Configurar el tamaño del canvas según el tamaño especificado en el HTML

// Las etiquetas son las que van en el eje X. 
const etiquetas = ["Superior", "Alto", "Medio", "Bajo"]
// Podemos tener varios conjuntos de datos. Comencemos con uno
const datosVentas2020 = {
    label: "Porcentaje de resultados en las Pruebas Saber 2022 - Pasto",
    data: [15.46, 23.71, 49.48, 11.34], // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
    backgroundColor: 'white', // Nuevo color de fondo más verde
    borderColor: 'black', // Nuevo color del borde más verde
    borderWidth: 1,// Ancho del borde
};

new Chart($grafica, {
    type: 'bar',// Tipo de gráfica
    data: {
        labels: etiquetas,
        datasets: [
            datosVentas2020,
            // Aquí más datos...
        ]
    },
    options: {
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 18, // Tamaño del texto de la leyenda aumentado a 16px
                    }
                }
            }
        },
        scales: {
            y: {
                ticks: {
                    beginAtZero: true,
                    font: {
                        size: 18, // Tamaño del texto del eje Y aumentado a 18px
                        color: 'rgba(0, 0, 0, 2)' // Color del texto del eje Y más oscuro
                    }
                }
            },
            x: { // Añadir configuración para el eje X (etiquetas)
                ticks: {
                    font: {
                        size: 18, // Tamaño del texto del eje X aumentado a 18px
                        color: 'rgba(0, 0, 0, 2)' // Color del texto del eje X más oscuro
                    }
                }
            }
        },
    }
});
