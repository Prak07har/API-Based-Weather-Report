from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

root = Tk()
root.title("Weather App")
root.geometry("600x700")
root['background'] = "aqua"


# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I:%M %p'), bg='white', font=("bold", 15))
hour.place(x=10, y=160)



# City Search
city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, sticky=W+E+N+S)

def fetch_weather():
    try:
        # API Call
        api_request = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city_entry.get()
            + "&units=metric&appid=5e5611bf09d48a590332a8f12aba882b"
        )
        api = api_request.json()

        # Temperatures
        y = api['main']
        current_temperature = y['temp']
        humidity = y['humidity']
        tempmin = y['temp_min']
        tempmax = y['temp_max']

        # Coordinates
        x = api['coord']
        longitude = x['lon']
        latitude = x['lat']

        # Country
        z = api['sys']
        country = z['country']
        city = api['name']

        # Updating the received info into the screen
        label_temp.configure(text=f"{current_temperature}°C")
        label_humidity.configure(text=f"{humidity}%")
        max_temp.configure(text=f"{tempmax}°C")
        min_temp.configure(text=f"{tempmin}°C")
        label_lon.configure(text=f"Lon: {longitude}")
        label_lat.configure(text=f"Lat: {latitude}")
        label_country.configure(text=country)
        label_city.configure(text=city)
    except Exception as e:
        label_city.configure(text="Error fetching data")

# Search Bar and Button
city_name_button = Button(root, text="Search", command=fetch_weather)
city_name_button.grid(row=1, column=1, padx=5, sticky=W+E+N+S)

# Country Names and Coordinates
label_city = Label(root, text="...", bg='white', font=("bold", 15))
label_city.place(x=11, y=63)

label_country = Label(root, text="...", bg='white', font=("bold", 15))
label_country.place(x=135, y=63)

label_lon = Label(root, text="...", bg='white', font=("Helvetica", 15))
label_lon.place(x=25, y=95)

label_lat = Label(root, text="...", bg='white', font=("Helvetica", 15))
label_lat.place(x=100, y=95)

# Current Temperature
label_temp = Label(root, text="...", bg='white', font=("Helvetica", 110), fg='black')
label_temp.place(x=18, y=220)

# Other temperature details
humi = Label(root, text="Humidity: ", bg='white', font=("bold", 15))
humi.place(x=3, y=400)

label_humidity = Label(root, text="...", bg='white', font=("bold", 15))
label_humidity.place(x=107, y=400)

maxi = Label(root, text="Max. Temp.: ", bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(root, text="...", bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="Min. Temp.: ", bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(root, text="...", bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

# Note
note = Label(root, text="All temperatures in degrees Celsius", bg='white', font=("italic", 10))
note.place(x=95, y=495)

root.mainloop()
