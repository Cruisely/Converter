import tkinter as tk
from tkinter import ttk

# Weight Conversion
def convert_weight():
    weight_value = float(weight_input.get())
    selected_unit = weight_combobox.get()

    if selected_unit == "Kg":
        converted = weight_value * 2.20462
        result_label.config(text="The Converted Weight is {:.2f} lbs".format(converted))
    elif selected_unit == "Lbs":
        converted = weight_value / 2.20462
        result_label.config(text="The Converted Weight is {:.2f} kg".format(converted))

# Time Conversion
def convert_time():
    time_value = float(time_input.get())
    selected_unit = time_combobox.get()
    converted_unit = converted_unit_combobox.get()

    conversion_factors = {
        "ms": 1,
        "s": 1000,
        "m": 60000,
        "h": 3600000,
        "d": 86400000
    }

    if selected_unit in conversion_factors and converted_unit in conversion_factors:
        converted = time_value * conversion_factors[selected_unit] / conversion_factors[converted_unit]
        result_label.config(text="The Converted Time is {:.2f} {}".format(converted, converted_unit))
    else:
        result_label.config(text="Invalid conversion unit.")

# Temperature Conversion
def convert_temperature():
    temperature_value = float(temperature_input.get())
    selected_unit = temperature_combobox.get()

    if selected_unit == "C":
        converted = temperature_value * 1.8 + 32
        result_label.config(text="The Converted Temperature is {:.2f} F".format(converted))
    elif selected_unit == "F":
        converted = (temperature_value - 32) / 1.8
        result_label.config(text="The Converted Temperature is {:.2f} C".format(converted))

# Speed Conversion
def convert_speed():
    speed_value = float(speed_input.get())
    selected_unit = speed_combobox.get()

    if selected_unit == "Kph":
        converted = speed_value / 1.60934
        result_label.config(text="The Converted Speed is {:.2f} mph".format(converted))
    elif selected_unit == "Mph":
        converted = speed_value * 1.60934
        result_label.config(text="The Converted Speed is {:.2f} kph".format(converted))

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Create the conversion type selection
conversion_type_label = tk.Label(window, text="Conversion Type:")
conversion_type_label.pack()

conversion_types = ["Weight", "Time", "Temperature", "Speed"]
conversion_type_combobox = ttk.Combobox(window, values=conversion_types, state="readonly")
conversion_type_combobox.current(0)
conversion_type_combobox.pack()

# Create the frames for each conversion type
weight_frame = tk.Frame(window)
time_frame = tk.Frame(window)
temperature_frame = tk.Frame(window)
speed_frame = tk.Frame(window)

# Weight Conversion
weight_label = tk.Label(weight_frame, text="Enter the Weight:")
weight_label.pack()

weight_input = tk.Entry(weight_frame)
weight_input.pack()

weight_combobox_label = tk.Label(weight_frame, text="Unit:")
weight_combobox_label.pack()

weight_units = ["Kg", "Lbs"]
weight_combobox = ttk.Combobox(weight_frame, values=weight_units, state="readonly")
weight_combobox.current(0)
weight_combobox.pack()

weight_button = tk.Button(weight_frame, text="Convert", command=convert_weight)
weight_button.pack()

# Time Conversion
time_label = tk.Label(time_frame, text="Enter the Time:")
time_label.pack()

time_input = tk.Entry(time_frame)
time_input.pack()

time_combobox_label = tk.Label(time_frame, text="Unit:")
time_combobox_label.pack()

time_units = ["ms", "s", "m", "h", "d"]
time_combobox = ttk.Combobox(time_frame, values=time_units, state="readonly")
time_combobox.current(0)
time_combobox.pack()

converted_unit_combobox_label = tk.Label(time_frame, text="Convert to:")
converted_unit_combobox_label.pack()

converted_units = ["ms", "s", "m", "h", "d"]
converted_unit_combobox = ttk.Combobox(time_frame, values=converted_units, state="readonly")
converted_unit_combobox.current(0)
converted_unit_combobox.pack()

time_button = tk.Button(time_frame, text="Convert", command=convert_time)
time_button.pack()

# Temperature Conversion
temperature_label = tk.Label(temperature_frame, text="Enter the Temperature:")
temperature_label.pack()

temperature_input = tk.Entry(temperature_frame)
temperature_input.pack()

temperature_combobox_label = tk.Label(temperature_frame, text="Unit:")
temperature_combobox_label.pack()

temperature_units = ["C", "F"]
temperature_combobox = ttk.Combobox(temperature_frame, values=temperature_units, state="readonly")
temperature_combobox.current(0)
temperature_combobox.pack()

temperature_button = tk.Button(temperature_frame, text="Convert", command=convert_temperature)
temperature_button.pack()

# Speed Conversion
speed_label = tk.Label(speed_frame, text="Enter the Speed:")
speed_label.pack()

speed_input = tk.Entry(speed_frame)
speed_input.pack()

speed_combobox_label = tk.Label(speed_frame, text="Unit:")
speed_combobox_label.pack()

speed_units = ["Kph", "Mph"]
speed_combobox = ttk.Combobox(speed_frame, values=speed_units, state="readonly")
speed_combobox.current(0)
speed_combobox.pack()

speed_button = tk.Button(speed_frame, text="Convert", command=convert_speed)
speed_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Initially pack the weight frame
weight_frame.pack()

def update_frame():
    selected_conversion_type = conversion_type_combobox.get()

    weight_frame.pack_forget()
    time_frame.pack_forget()
    temperature_frame.pack_forget()
    speed_frame.pack_forget()

    if selected_conversion_type == "Weight":
        weight_frame.pack()
    elif selected_conversion_type == "Time":
        time_frame.pack()
    elif selected_conversion_type == "Temperature":
        temperature_frame.pack()
    elif selected_conversion_type == "Speed":
        speed_frame.pack()

conversion_type_combobox.bind("<<ComboboxSelected>>", lambda event: update_frame())

# Run the main window loop
window.mainloop()
