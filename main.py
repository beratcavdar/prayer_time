import requests
import tkinter as tk

window = tk.Tk()
window.title("Prayer Time")
window.config(background="light green")

latitude_label = tk.Label(text="Enter latitude:")
latitude_entry = tk.Entry()
longitude_label = tk.Label(text="Enter longitude:")
longitude_entry = tk.Entry()
finding_button = tk.Button(text="Find it :D", command=lambda: fetch_prayer_times())
response = tk.Text(width=80, height=15)

latitude_label.pack(pady=10)
latitude_entry.pack(pady=5)
longitude_label.pack(pady=5)
longitude_entry.pack(pady=5)
finding_button.pack(pady=5)
response.pack(pady=5)

def get_prayer_times(latitude, longitude):
    base_url = f"http://api.aladhan.com/v1/calendar"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "method": 2,  # Calculation method (2 for Islamic Society of North America)
        "month": 8,   # Example month
        "year": 2023, # Example year
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["code"] == 200:
        return data["data"][0]["timings"]
    else:
        return None

def display_prayer_times(prayer_times):
    if prayer_times is None:
        return "Failed to retrieve prayer times."

    result = "Prayer Times:\n"
    for prayer, time in prayer_times.items():
        result += f"{prayer}: {time}\n"
    return result

def fetch_prayer_times():
    latitude = float(latitude_entry.get())
    longitude = float(longitude_entry.get())

    prayer_times = get_prayer_times(latitude, longitude)
    response.delete(1.0, tk.END)  # Clear previous result
    response.insert(tk.END, display_prayer_times(prayer_times))

tk.mainloop()
