import datetime
import api
import tkinter as tk
import geopy
import requests
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import ttkbootstrap


def get_weather(city):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api.API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = round(weather['main']['temp'] - 273.15, 2)
    description = weather['weather'][0]['description']
    mainweather = weather['weather']['main']
    city = weather['name']
    country = weather['sys']['country']



    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url, temperature, description, city, country, mainweather)

# def forecast(city):
#     from geopy.geocoders import Nominatim


#     geolocator = Nominatim(user_agent="MyApp")

#     location = geolocator.geocode(f"{city}")
#     lat, lon = location.latitude, location.longitude
#     forecast_url =  f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={api.API_key}"
#     res = requests.get(forecast_url)

#     if res.status_code == 404:
#         messagebox.showerror("Error", "Forecast not found")
#         return None
    
#     response = res.json()
    
    
#     daily_forecasts = []
#     for daily_data in response['daily'][:5]:
#         icon2_id = daily_data['weather'][0]['icon']
#         daily_forecasts.append({
#             'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
#             'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
#             'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
#             'description': daily_data['weather'][0]['description'],
#             "icon_url" : f"https://openweathermap.org/img/wn/{icon2_id}@2x.png",
#         })

#     return(daily_forecasts)

   


    
def search():
    city = city_fill.get()
    result = get_weather(city)
    if result is None:
        return 0
    
    icon_url, temperature, description, city, country, mainweather = result
    location_label.configure(text=f"{city}, {country}")

    image1 = Image.open(requests.get(icon_url, stream=True).raw)
    icon1 = ImageTk.PhotoImage(image1)
    icon_label.configure(image=icon1)
    icon_label.image = icon1

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

    status_label.configure(text=f"real-time-status: {mainweather}")
    
    

root = ttkbootstrap.Window(themename="journal")
root.title("Weather App")
root.geometry("600x800")

city_fill = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_fill.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

status_label = tk.Label(root, font="Helvetica, 20")
status_label.pack()
root.mainloop()