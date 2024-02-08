import tkinter as tk
from tkinter import ttk, messagebox

# Copyright and license text
license_text = """Copyright (c) 2024 Roberto Cimmino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# Function to display the license information
def show_license():
    # Create a new Toplevel window to display the license information
    license_window = tk.Toplevel(window)
    license_window.title("License Information")
    license_window.geometry("700x450")  # Adjust window size
    license_window.resizable(False, False)

    # Create a scrollable text widget to display the license text
    license_text_widget = tk.Text(license_window, wrap="word")
    license_text_widget.pack(fill="both", expand=True)

    # Insert the license text into the text widget
    license_text_widget.insert("1.0", license_text)
    
    # Disable text widget to prevent editing
    license_text_widget.config(state="disabled")

# Create Tkinter window with adjusted initial width
window = tk.Tk()
window.title("Unit Converter")
window.geometry("250x200")  # this size is ideal
window.option_add("*Font", "Helvetica 13")  # Set font size to 13 points

# Create a label for the app title
app_title_label = tk.Label(window, text="Unit Converter by Roberto Cimmino", font=("Helvetica", 12))
app_title_label.pack(pady=3)

# Center the main window of the application on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"+{x}+{y}")

# Display the initial message when the program starts
messagebox.showinfo("Licence", "2024 by Roberto Cimmino Creative Common CC BY-NC-SA 4.0")

# Entry field for the value to be converted
value_var = tk.StringVar()
value_entry = tk.Entry(window, textvariable=value_var)
value_entry.pack(pady=3)

# Include all the conversion functions here
# Temperature Conversions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Mass Conversions
def ounces_to_grams(ounces):
    return ounces * 28.3495

def grams_to_ounces(grams):
    return grams * 0.035274

def pounds_to_grams(pounds):
    return pounds * 453.592

def grams_to_pounds(grams):
    return grams * 0.00220462

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def grams_to_lbs(grams):
    return grams * 0.00220462  # 1 gram is approximately 0.00220462 pounds

# Additional mass conversion helpers

# Volume Conversions
def cups_to_milliliters(cups):
    return cups * 236.588

def liters_to_cups(cups):
    return cups * 4.22675

# Conversion Functions (Paste all the provided conversion functions here)

# The updated convert function now only needs to handle conversion logic
def auto_convert(*args):
    try:
        value = float(value_var.get())
        if conversion_type.get() == "C° to F°":
            conversion_result = celsius_to_fahrenheit(value)
        elif conversion_type.get() == "F° to C°":
            conversion_result = fahrenheit_to_celsius(value)
        elif conversion_type.get() == "Oz to Grams":
            conversion_result = ounces_to_grams(value)
        elif conversion_type.get() == "Grams to Oz":
            conversion_result = grams_to_ounces(value)
        elif conversion_type.get() == "Grams to Lb":
            conversion_result = grams_to_lbs(value)
        elif conversion_type.get() == "Lb to Grams":
            conversion_result = pounds_to_grams(value)
        elif conversion_type.get() == "Lb to Kg":
            conversion_result = pounds_to_kilograms(value)
        elif conversion_type.get() == "Kg to Lb":
            conversion_result = kilograms_to_pounds(value)
        elif conversion_type.get() == "Cups to Ml":
            conversion_result = cups_to_milliliters(value)
        elif conversion_type.get() == "Lt to Cups":
            conversion_result = liters_to_cups(value)

        # Include additional elif blocks here for each conversion type
        else:
            conversion_result = "Unsupported conversion."

        result_label.config(text=f"Result: {conversion_result}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Dropdown menu for conversion type selection and its tracing setup
conversion_type = tk.StringVar()
conversion_choices = [
    "C° to F°", 
    "F° to C°",
    "Oz to Grams",
    "Grams to Oz",
    "Grams to Lb",
    "Lb to Grams",
    "Lb to Kg",
    "Kg to Lb",
    "Cups to Ml",
    "Lt to Cups",
]

conversion_type.set(conversion_choices[0])  # set the default option
conversion_menu = ttk.Combobox(window, textvariable=conversion_type, values=conversion_choices, state="readonly")
conversion_menu.pack(pady=3)
conversion_type.trace('w', auto_convert)  # Trace changes

# Label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=3)

# Variable to track the "Always on Top" state
always_on_top_var = tk.BooleanVar()
always_on_top_var.set(False)  # Default: not always on top

# Function to toggle "Always on Top" mode
def toggle_always_on_top():
    window.attributes("-topmost", always_on_top_var.get())

# Checkbutton to toggle "Always on Top" mode
always_on_top_checkbutton = tk.Checkbutton(window, text="Always on Top", var=always_on_top_var, command=toggle_always_on_top)
always_on_top_checkbutton.pack(pady=3)

# Create a button to display the license information
license_button = tk.Button(window, text="View License", command=show_license)
license_button.pack(pady=3)

# Run the Tkinter event loop
window.mainloop()