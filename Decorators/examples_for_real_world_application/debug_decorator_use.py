from debug_decorator import debug
import math

math.factorial = debug(math.factorial)


def apporximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


print(apporximate_e(5))