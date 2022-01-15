# Convert a temp from 'f' to 'c' or back again
# Michael Powe
# 20220115T112859

"""
Convert temperatures from Celsius to Fahrenheit or the reverse.
Usage: python ./convert_temp.py
Follow the prompts
"""
from TempConverter import *


def notice():
    print(
        """
          =================================================
          Temperature conversion from Celsius to Fahrenheit
                           and vice versa.
                         (c)2022 Michael Powe
                      "Baby, it's cold outside!"
          =================================================

        """
    )


def main():

    notice()

    # for validating input, i.e., rejecting any other entries
    types = ("F", "C")

    print("What temperature to convert? ")
    temp = float(input())

    print("What system to convert from ('c' or 'f')")
    from_type = input().upper()

    # Capture direction of the conversion
    to_type = "F" if from_type == "C" else "C"

    new_temp = TempConverter.convert(temp, from_type)

    # Only print if the correct temperature type is used
    # Otherwise, the converter returns an error message, don't need one here
    if from_type in types:
        print("{:.1f}°{} is {:.1f}°{} ".format(temp, from_type, new_temp, to_type))


main()
# end of script
