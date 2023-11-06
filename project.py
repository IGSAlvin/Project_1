import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    API_key = ""
    url = f""
    res = requests.get(url)
    
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