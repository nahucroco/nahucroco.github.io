const api_key = '7997aeeb83d69f69a78de36d549ee2be';

const fetchData = position => {
    const { latitude, longitude } = position.coords;
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&lang=sp&appid=${api_key}&units=metric`)
        .then(response => response.json())
        .then(data => setWeatherData(data))

}

const setWeatherData = data => {
    console.log(data);
    const weatherData = {
        location: data.name,
        description: data.weather[0].main,
        humidity: data.main.humidity + '%',
        pressure: data.main.pressure + ' mbar',
        temperature: data.main.temp + 'º',
        date: getDate(),
    }

    Object.keys(weatherData).forEach( key =>{
        document.getElementById(key).textContent = weatherData[key];
    });

    cleanUp();
}

const cleanUp = () => {
    let container = document.getElementById('container');
    let loader = document.getElementById('loader');

    loader.style.display = 'none';
    container.style.display = 'flex';
}

const getDate = () => {
    let date = new Date();
    return `${date.getDate()}-${('0' + (date.getMonth() + 1)).slice(-2)}-${date.getFullYear()}`;
}



const onLoad = () =>{
    navigator.geolocation.getCurrentPosition(fetchData);
}

const getUbi = () => {
    let ubicacion = document.getElementById('ubicacion').value;
    console.log(ubicacion);
}

getUbi();