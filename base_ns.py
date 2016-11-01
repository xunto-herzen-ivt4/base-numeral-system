import math


def convert(number, target_base):
    result = []
    while number >= target_base:
        result.append(number % target_base)
        number = math.floor(number / target_base)
    result.append(number)
    result.reverse()
    return result


def convert_to_dec(array, source_base):
    result = 0
    for item in array:
        result *= source_base
        result += item
    return result

