import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    API_key = "b103be549427acf08923cf74d502efda"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("error", "City not found")
        return None
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather']['0']['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url, temperature, description, city, country)

def city_search():
    city = city_fill.get()
    result = get_weather(city)
    if result is None:
        return


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

city_fill = ttkbootstrap.Entry(root, font="Arial, 14")
city_fill.pack(pady=10)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.label(root, font="Arial, 16")
temperature_label.pack()

description_label = tk.Label(root, font="Arial, 16")