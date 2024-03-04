import tkinter as tk
import requests

# Replace with your own API key from OpenWeatherMap
API_KEY = "f65e1bddc73a3ef3cc0b7ba58810033a"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    if weather_data is not None:
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temp = round(weather_data["main"]["temp"] - 273.15, 1) # Convert from Kelvin to Celsius
        description = weather_data["weather"][0]["description"]

        result_label.config(text=f"City: {city}, Country: {country}\nTemperature: {temp}°C\nDescription: {description}")
    else:
        result_label.config(text="Error: City not found")

# Create the window
window = tk.Tk()
window.title("Weather App")

# Create a label for the result
result_label = tk.Label(window, font=("Arial", 16))
result_label.pack(pady=20)

# Create a label and entry for the city name
city_label = tk.Label(window, text="Enter city name:", font=("Arial", 14))
city_label.pack()
city_entry = tk.Entry(window, font=("Arial", 14), width=20)
city_entry.pack(pady=10)

# Create a button to get the weather data
button = tk.Button(window, text="Get Weather", font=("Arial", 14), command=lambda: display_weather(get_weather_data(city_entry.get())))
button.pack(pady=10)

# Start the main loop
window.mainloop()