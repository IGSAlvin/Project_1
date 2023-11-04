import tkinker as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

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