document.addEventListener("DOMContentLoaded", () => {
    fetchWeatherData();
    fetchAlerts();
  });
  
  function fetchWeatherData() {
    fetch("/api/weather-summary")
      .then(response => response.json())
      .then(data => {
        document.getElementById("summary-data").innerHTML = `
          <p>Temperature: ${data.temp} °C</p>
          <p>Feels Like: ${data.feels_like} °C</p>
          <p>Main: ${data.main}</p>
        `;
      })
      .catch(error => console.error("Error fetching weather data:", error));
  }
  
  function fetchAlerts() {
    fetch("/api/alerts")
      .then(response => response.json())
      .then(data => {
        document.getElementById("alert-data").innerHTML = `
          <p>${data.message}</p>
        `;
      })
      .catch(error => console.error("Error fetching alerts:", error));
  }
  