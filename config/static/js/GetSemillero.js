document.addEventListener("DOMContentLoaded", function () {
    const semillerosTable = document.getElementById("semillerosTable");
    let endpoint = "/GetSemillero";
    // Realizar una solicitud GET a tu API
    axios.get(endpoint)  
        .then(function (response) {
            const semilleros = response.data.semilleros_investigacion;

            semilleros.forEach(function (semillero) {
                const row = document.createElement("tr");

                // Rellenar las celdas de la fila con datos de la respuesta API
                row.innerHTML = `
                    <td>${semillero["Nombre del Grupo de Investigación"]}</td>
                    <td>${semillero["Líder del Grupo de Investigación"]}</td>
                    <td>${semillero["Nombre del Semillero"]}</td>
                    <td>${semillero["Periodo Académico"]}</td>
                    <td>${semillero["Docente líder del semillero"]}</td>
                    <td>${semillero["Proyectos"].join(", ")}</td>
                    <td>${semillero["Objetivos"].join(", ")}</td>
                    <td>${semillero["Resultados Obtenidos"].join(", ")}</td>
                    <td>${semillero["Estudiantes"].join(", ")}</td>
                    <td>${semillero["Profesores"].join(", ")}</td>
                `;

                semillerosTable.appendChild(row);
            });
        })
        .catch(function (error) {
            console.error("Error al obtener datos de la API: " + error);
        });
});
