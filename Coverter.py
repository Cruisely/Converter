#weight
import unittest


def weight():
    unit = input ('Would you like to convert to Kg or Lbs? ')
    weight = int(input('Enter The Weight You Would Like to Convert: '))
    if unit.lower() == 'lbs':
        converted = weight / 0.45
        print("The Converted Weight is " + str(converted) + " Lbs")
    else:
        converted = weight * 0.45
        print("The Converted Weight is " + str(converted) + " Kg")
        input("Press enter to exit")

#Duration
def time():
    millisecond = "ms"
    second = "s"
    minute = "m"
    hour = "h"
    day = "d"

    time = int(input('Enter the Time You Would Like to Convert: '))
    unit = input('ms, s, m, h, or d? ')
    converted_unit = input('Would You Like to Convert to ms, s, m, h, or d? ')

    if unit.lower() == "ms":
        if converted_unit.lower() == "ms":
            converted = time
            print("The Converted Time is " + str(converted) + millisecond)
        elif converted_unit.lower() == "s":
            converted = time / 1000
            print("The Converted Time is " + str(converted) + second)
        elif converted_unit.lower() == "m":
            converted = time / 60000
            print("The Converted Time is " + str(converted) + minute)
        elif converted_unit.lower() == "h":
            converted = time / 3600000
            print("The Converted Time is " + str(converted) + hour)
        elif converted_unit.lower() == "d":
            converted = time / 86400000
            print("The Converted Time is " + str(converted) + day)
        else:
            print("Invalid conversion unit.")
    elif unit.lower() == "s":
        if converted_unit.lower() == "ms":
            converted = time * 1000
            print("The Converted Time is " + str(converted) + millisecond)
        elif converted_unit.lower() == "s":
            converted = time
            print("The Converted Time is " + str(converted) + second)
        elif converted_unit.lower() == "m":
            converted = time / 60
            print("The Converted Time is " + str(converted) + minute)
        elif converted_unit.lower() == "h":
            converted = time / 3600
            print("The Converted Time is " + str(converted) + hour)
        elif converted_unit.lower() == "d":
            converted = time / 86400
            print("The Converted Time is " + str(converted) + day)
        else:
            print("Invalid conversion unit.")
    elif unit.lower() == "m":
        if converted_unit.lower() == "ms":
            converted = time * 60000
            print("The Converted Time is " + str(converted) + millisecond)
        elif converted_unit.lower() == "s":
            converted = time * 60
            print("The Converted Time is " + str(converted) + second)
        elif converted_unit.lower() == "m":
            converted = time
            print("The Converted Time is " + str(converted) + minute)
        elif converted_unit.lower() == "h":
            converted = time / 60
            print("The Converted Time is " + str(converted) + hour)
        elif converted_unit.lower() == "d":
            converted = time / 1440
            print("The Converted Time is " + str(converted) + day)
        else:
            print("Invalid conversion unit.")
    elif unit.lower() == "h":
        if converted_unit.lower() == "ms":
            converted = time * 3600000
            print("The Converted Time is " + str(converted) + millisecond)
        elif converted_unit.lower() == "s":
            converted = time * 3600
            print("The Converted Time is " + str(converted) + second)
        elif converted_unit.lower() == "m":
            converted = time * 60
            print("The Converted Time is " + str(converted) + minute)
        elif converted_unit.lower() == "h":
            converted = time
            print("The Converted Time is " + str(converted) + hour)
        elif converted_unit.lower() == "d":
            converted = time / 24
            print("The Converted Time is " + str(converted) + day)
        else:
            print("Invalid conversion unit.")
    elif unit.lower() == "d":
        if converted_unit.lower() == "ms":
            converted = time * 86400000
            print("The Converted Time is " + str(converted) + millisecond)
        elif converted_unit.lower() == "s":
            converted = time * 86400
            print("The Converted Time is " + str(converted) + second)
        elif converted_unit.lower() == "m":
            converted = time * 1440
            print("The Converted Time is " + str(converted) + minute)
        elif converted_unit.lower() == "h":
            converted = time * 24
            print("The Converted Time is " + str(converted) + hour)
        elif converted_unit.lower() == "d":
            converted = time
            print("The Converted Time is " + str(converted) + day)
        else:
            print("Invalid conversion unit.")
    else:
        print("Invalid input unit.")

    input("Press enter to exit")

#Temperature
def temperature():
    unit = input('Would you like to convert to C or F? ')
    Temperature = float(input('Enter the Temperature You Would Like to Convert: '))
    if unit.lower() == "f":
        converted = Temperature * (1.8) + 32
        print("The Converted Temperature is " + str(converted) + " F")
    else:
        converted = Temperature - 32
        converted / (1.8)
        print("The Converted Temperature is " + str(converted) + " C")
        input("Press enter to exit")

#Speed
def speed():
    unit = input ('Are you converting from Kph or Mph? ')
    speed = float(input('Enter The Speed You Would Like to Convert: '))
    if unit.lower() == 'kph':
        converted = speed / 1.609344 
        print("The Converted speed is " + str(converted) + " Mph")
    else:
        converted = speed * 1.6093440006147
        print("The Converted speed is " + str(converted) + " Kph")
        input("Press enter to exit")

def main():
  choic = input('Do You Want to Convert Weight, Time, Temperature, or Speed? ')
  if choic == 'weight':
    weight()
  if choic == 'time':
    time()
  if choic == 'speed':
    speed()
  elif choic == 'temp':
    temperature()

main()