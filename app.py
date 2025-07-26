import requests
from tkinter import Tk, Canvas, Entry, Button, StringVar
from PIL import Image, ImageTk

def get_weather():
    city = city_var.get().strip()
    if not city:
        display_error("Please enter a city.")
        return

    api_key = "your api key"
    url = f"open weather app"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            display_results(
                city_name,
                [
                    f"Temperature: {temp}°C",
                    f"Humidity: {humidity}%"
                ],
                description
            )
        else:
            display_error("City not found. Please try again.")
    except Exception:
        display_error("Error fetching data.")

def display_results(city_name, data, description):
    canvas.delete("result")

    # City name (large)
    canvas.create_text(
        250, 250, text=city_name, font=("Arial", 18, "bold"),
        fill="#051f34", tag="result"
    )

    # Horizontal line
    canvas.create_line(50, 270, 450, 270, fill="#051f34", width=2, tag="result")

    # Temp & Humidity on same line
    canvas.create_text(
        160, 300, text=data[0], font=("Arial", 16),
        fill="#294549", tag="result"
    )
    canvas.create_text(
        340, 300, text=data[1], font=("Arial", 16),
        fill="#294549", tag="result"
    )

    # Description on separate line
    canvas.create_text(
        250, 340, text=f"Description: {description.capitalize()}",
        font=("Arial", 12), fill="#01528a", tag="result"
    )

def display_error(message):
    canvas.delete("result")
    canvas.create_text(
        250, 280, text=message, font=("Arial", 12), fill="red", tag="result"
    )

# GUI setup
root = Tk()
root.title("Weather App")
root.geometry("500x500")
root.resizable(False, False)

# Background image
background_image = Image.open("background.jpg")  # Replace with your image path
background_image = background_image.resize((500, 500))
bg_photo = ImageTk.PhotoImage(background_image)

canvas = Canvas(root, width=500, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Variables
city_var = StringVar()

# Static UI text
canvas.create_text(250, 50, text="Weather App", font=("Helvetica", 20, "bold"), fill="white")
canvas.create_text(250, 100, text="Enter City:", font=("Arial", 12, "bold"), fill="white")

# Entry box
entry_widget = Entry(root, textvariable=city_var, font=("Arial", 12), justify="center")
canvas.create_window(250, 130, window=entry_widget, width=200, height=30)

# Button
canvas.create_window(250, 170, window=Button(
    root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="lightblue"
), width=120, height=30)

root.mainloop()
