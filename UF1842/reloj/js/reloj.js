let manejador;

function mostarhora() {

    let fecha = new Date();
    let hora = fecha.getHours();
    let minutos = fecha.getMinutes();
    let segundos = fecha.getSeconds();

    let spanHora = document.getElementById("hora");
    let spanMinutos = document.getElementById("minutos");
    let spanSegundos = document.getElementById("segundos");

    spanHora.innerHTML = hora.toString().padStart(2, '0');
    spanMinutos.innerHTML = String(minutos).padStart(2, '0');
    spanSegundos.innerHTML = (segundos < 10) ? "0" + segundos : segundos;
}

function iniciarReloj() {
    mostarhora();
    manejador = setInterval(mostarhora, 1000);
}
function pararReloj() {
    clearInterval(manejador);
    
}
  
function mostarfecha() {
    let fecha = new Date();
    let dia = fecha.getDate();
    let mes = fecha.getMonth() + 1;
    let diasemana = fecha.getDay();

    let spanDia = document.getElementById("dia");
    let spanMes = document.getElementById("mes");
    let spanDiasemana = document.getElementById("diaSemana");

    spanDia.innerHTML = dia.toString().padStart(2, '0');
    spanMes.innerHTML = String(mes).padStart(2, '0');
    spanDiasemana.innerHTML = diaSemana(diasemana);
    // spanDiaSemana.innerHTML = (diaSemana == 1) ? "Lunes" : (diaSemana == 2) ? "Martes" : (diaSemana == 3) ? "Miércoles" : (diaSemana == 4) ? "Jueves" : (diaSemana == 5) ? "Viernes" : (diaSemana == 6) ? "Sábado" : "Domingo";
}

function diaSemana(numDia) {
    let semana = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sab'];
    return semana[numDia].toUpperCase();
}

function temperaturaHumedad() {
    fetch('https://api.open-meteo.com/v1/forecast?latitude=40.42&longitude=-3.70&current_weather=true&hourly=temperature_2m,relative_humidity_2m')
        .then(response => response.json())
        .then(data => {
            let temperatura = data.current_weather.temperature;
            let humedad = data.hourly.relative_humidity_2m[0];
            document.getElementById("temperatura").innerHTML = temperatura.toString().padStart(2, '0');
            document.getElementById("humedad").innerHTML = humedad.toString().padStart(2, '0');
        })
        .catch(error => console.error('Error al obtener los datos del clima:', error));
}
temperaturaHumedad();
mostarhora();
mostarfecha();