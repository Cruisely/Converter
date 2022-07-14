#weight
from tkinter import END


def weight():
    weight = int(input('Enter The Weight You Would Like to Convert: '))
    unit = input ('Kg or Lbs ')
    if unit.upper() == 'Kg':
        converted = weight / 0.45
        print("The Converted Weight in Lbs is " + str(converted))
    else:
        converted = weight * 0.45
        print("The Converted Weight in Kg is " + str(converted))
        input("Press enter to exit")

#Time
#WIP
def time():
  time = float(input('Enter the Time You Would Like to Convert? '))
  unit = input ('ms, s, m, h, or d? ')
  time = float(input('What Would You Like to Convert to? '))
  unit2 = input ('ms, s, m, h, or d?')
  if unit.upper() == "ms":
    converted = weight * 1000
    print("The Converted Time is " + float(converted))
  else:
    converted = weight * 0.45
    print("The Converted Time in UNIT is " + float(converted))
    input("Press enter to exit")

#Temperature
def temperature():
    Temperature = int(input('Enter the Temperature You Would Like to Convert '))
    unit = input ('C or F ')
    if unit.upper() == "C":
        converted = Temperature * (1.8) + 32
        print("The Converted Temperature in F is " + str(converted))
    else:
        converted = Temperature - 32
        converted / (1.8)
        print("The Converted Temperature in C is " + str(converted))
        input("Press enter to exit")

def main():
  choic = input('Do You Want to Convert Weight, Time or Temperature? ')
  if choic == 'weight':
    weight()
  if choic == 'time':
    time()
  elif choic == 'temp':
    temperature()

main()