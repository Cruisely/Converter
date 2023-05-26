milliseconds = "ms"
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
        print("The Converted Time is " + str(converted) + milliseconds)
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
        print("The Converted Time is " + str(converted) + milliseconds)
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
        print("The Converted Time is " + str(converted) + milliseconds)
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
        print("The Converted Time is " + str(converted) + milliseconds)
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
        print("The Converted Time is " + str(converted) + milliseconds)
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
