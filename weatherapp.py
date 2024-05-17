import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    api_key = "0207e3b4f0c19dde312ac11bb5aa3855"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        weather_info = f"Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {description}"
    else:
        weather_info = "City Not Found!"
    
    return weather_info

def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "Please enter a city name")

app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")

city_label = tk.Label(app, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=10)

show_button = tk.Button(app, text="Show Weather", command=show_weather)
show_button.pack(pady=10)

weather_label = tk.Label(app, text="", font=("Helvetica", 16), justify="left")
weather_label.pack(pady=20)

app.mainloop()

