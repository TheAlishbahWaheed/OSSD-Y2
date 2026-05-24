from scrapper import get_cars_data
import tkinter as tk
from tkinter import ttk
# improve the user interface creatively and use other widgets as well.
def set_textarea(data):
    textarea.delete(1.0, tk.END)

    for car in data:
        textarea.insert(
            tk.END,
            f"🚗 Name: {car['name']}\n💰 Price: {car['price']}\n\n"
        )
root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("600x400")
root.config(bg="#f0f4f7")
# Heading
title = tk.Label(
    root,
    text="🚘 Car Price Scraper",
    font=("Arial", 20, "bold"),
    bg="#f0f4f7",
    fg="darkblue"
)
title.pack(pady=15)
# Step 1
car_manufact = ['toyota', 'honda', 'suzuki']
dropdown = ttk.Combobox(root, values=car_manufact, font=("Arial", 12))
dropdown.current(2)
dropdown.pack(pady=10)
search_button = tk.Button( root, text="Search",  command=lambda: set_textarea(get_cars_data(dropdown.get())),  bg="darkblue", fg="white", font=("Arial", 11, "bold"),padx=10, pady=5)
search_button.pack(pady=10)
frame = tk.Frame(root)
frame.pack(pady=10)
scrollbar = tk.Scrollbar(frame)
textarea = tk.Text( frame, height=15, width=60, font=("Arial", 11), yscrollcommand=scrollbar.set, bg="white")
scrollbar.config(command=textarea.yview)
textarea.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
status = tk.Label(
    root,
    text="Select a brand and click Search",
    bg="#f0f4f7",
    fg="gray",
    font=("Arial", 10)
)
status.pack(pady=5)

root.mainloop()