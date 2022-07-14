from doctest import OutputChecker
import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title("EZ Converter")
root.geometry('500x500')

def weight():
    weight_val = weight_text.get("1.0",END)
    print(weight_val)

weight_val = int(input('Enter The Weight You Would Like to Convert: '))
unit = input ('Kg or Lbs ')
if unit.upper() == 'Kg':
    converted = weight_val / 0.45
    print("The Converted Weight in Lbs is " + str(converted))
else:
    converted = weight_val * 0.45
    output.insert(END,"The Converted Weight in Kg is " + str(converted))

weight_text = Text(root, 
                height = 1, 
                width =52)
#weight_text.insert(END, 'Enter Your Conversion')
weight_text.pack()

convert_button = Button(root, height = 2, 
                width = 20, 
                text = "Convert", command = weight)
convert_button.pack()

output = Text(root, height = 5, 
                width = 52, 
                bg = "#037ca8")
output.pack()

root.mainloop()