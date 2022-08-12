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

#Time
#WIP
def time():
    print("Work in Progress")
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