# convert from F to C and back again
# 20220113T100753
# Michael Powe

# F to C
# (F - 32) * 5/9 = C
# ((F -  32) * 5)/9 = C
#
# C to F
# (C * 9/5) + 32 = F
# (C * 9)/5 + 32 = F
#
# (F − 32) × 5/9 + 273.15 = K
# (((F - 32) * 5)/9) + 273.15 = K
# C° + 273.15 = K°


class TempConverter:
    """
    Class to convert a given temperature from a given type to the other type

    Usage: What temperature to convert?
           -273.15
           What system to convert from ('c' or 'f')
           c
           -273.1°C is -459.7°F

    Functions:
         convert(temperature, type) -> float

    Variables:
         default_temp
    """

    def __init__():
        pass

    default_temp: float = -9999.99

    @classmethod
    def convert(cls, temperature: float, type: str) -> float:

        type = type.upper()

        if type == "F":
            new_temp: float = ((temperature - 32) * 5) / 9
        elif type == "C":
            new_temp = (temperature * 9) / 5 + 32
        else:
            print("Invalid temperature type. It must be either 'F' or 'C'.")
            new_temp = cls.default_temp
            print("{}°{}".format(new_temp, type))

        return new_temp


# end TempConverter
