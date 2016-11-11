import math


class NumberBased:
    def __init__(self, base=-1, integer_converted=None, float_converted=None):
        self.base = base
        self.integer = integer_converted or [0]
        self.fraction = float_converted or [0]

    @staticmethod
    def __symbol__(number):
        symbol = str(number)
        if number > 9:
            symbol = '[' + symbol + ']'
        return symbol

    def __str__(self):
        return \
            ''.join(self.__symbol__(number) for number in self.integer) + \
            '.' + \
            ''.join(self.__symbol__(number) for number in self.fraction)


def convert(number: float, target_base: int, accuracy=6):
    assert number >= 0, "Only positive number is accepted."
    assert target_base >= 0, "Only positive base is accepted."

    converted = NumberBased(target_base)

    float_part, integer_part = math.modf(number)
    integer_part = int(integer_part)

    if integer_part > 0:
        converted.integer = __integer_convert_(integer_part, target_base)

    if float_part > 0:
        converted.fraction = __float_convert_(float_part, target_base, accuracy)
    return converted


def convert_to_dec(converted: NumberBased):
    base = converted.base

    integer_part = 0
    for num in converted.integer:
        integer_part *= base
        integer_part += num

    fraction_part = 0
    for num in converted.fraction:
        fraction_part /= base
        fraction_part += num / base

    return integer_part + fraction_part


def __integer_convert_(integer_part, target_base):
    integer_converted = []
    while integer_part >= target_base:
        integer_converted.append(integer_part % target_base)
        integer_part = math.floor(integer_part / target_base)
    integer_converted.append(integer_part)
    integer_converted.reverse()
    return integer_converted


def __float_convert_(float_part, target_base, accuracy):
    float_converted = []
    while float_part != 0 and len(float_converted) < accuracy:
        float_part *= target_base
        integer_part = int(float_part)
        float_converted.append(integer_part)
        if float_part >= 1:
            float_part -= integer_part
    return float_converted

