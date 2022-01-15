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


class TempConverter:
    """
    Class to convert a given temperature from a given type to the other type

    Usage: ~from TempConverter import *~

    Functions:
         convert(temp, type) -> float

    Variables:
         default_temp
    """

    def __init__():
        pass

    default_temp: float = 99.99

    @classmethod
    def convert(cls, temp: float, type: str) -> float:

        type = type.upper()

        if type == "F":
            new_temp = ((temp - 32) * 5) / 9
        elif type == "C":
            new_temp = (temp * 9) / 5 + 32
        else:
            print("Invalid temperature type. It must be either 'F' or 'C'.")
            new_temp = cls.default_temp

        return new_temp


# end TempConverter
