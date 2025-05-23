import tkinter as tk
from weather import get_weather

def show_weather():
    city = city_input.get()
    temp, description = get_weather(city)
    if temp is not None:
        temp_label.config(text=f"Temperature: {temp}°C")
        description_label.config(text=f"Description: {description}")
    else:
        temp_label.config(text="Temperature: N/A")
        description_label.config(text=f"Error: {description}")

window = tk.Tk()
window.title("Weather App")
window.geometry("300x250")
window.configure(bg="lightblue")

header = tk.Label(window, text="Weather App", font=("Arial", 24), bg="lightblue")
header.pack(pady=10)

city_label = tk.Label(window, text="Enter City:", font=("Arial", 14), bg="lightblue")
city_label.pack(pady=5)

city_input = tk.Entry(window, font=("Arial", 14), bg="white")
city_input.pack(pady=5)

get_weather_btn = tk.Button(window, text="Get Weather", font=("Arial", 14), command=show_weather)
get_weather_btn.pack(pady=5)

temp_label = tk.Label(window, text="Temperature: ", font=("Arial", 14), bg="lightblue")
temp_label.pack(pady=5)

description_label = tk.Label(window, text="Description: ", font=("Arial", 14), bg="lightblue")
description_label.pack(pady=5)

window.mainloop()