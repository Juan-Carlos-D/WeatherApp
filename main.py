from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def toggle_fullscreen():
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)

def getweather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="my_weather_app")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=227649c4bb5d628d94d35122c8b861a6"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        temp_str = f"{temp}°"
        condition_str = f"{condition} | FEELS LIKE {temp}"

        t.config(text=temp_str)
        c.config(text=condition_str)

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(True, True)

# search box
Search_image = PhotoImage(file="search.png")
my_image = Label(image=Search_image)
my_image.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
my_image_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getweather)
my_image_icon.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Frame for the labels
label_frame = Frame(root)
label_frame.place(x=0, y=400, width=900)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image, master=label_frame)
frame_myimage.pack(padx=5, pady=5, side=TOP)

# Time
name = Label(label_frame, font=("arial", 15, "bold"))
name.pack(side=LEFT, padx=20, pady=10)
clock = Label(label_frame, font=("Helvetica", 20))
clock.pack(side=LEFT, padx=20, pady=10)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=430)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=430)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=430)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=430)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=460)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=460)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=460)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=460)

# Toggle fullscreen button
fullscreen_button = Button(root, text="Toggle Screen", command=toggle_fullscreen)
fullscreen_button.place(x=800, y=10)

root.mainloop()


