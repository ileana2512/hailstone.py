# Author: Ileana Hernandez
# Date: 01/27/2021
# Description: Hailstone sequence

def hailstone_steps(num):
    """takes a positive integer in a hailstone sequence and
        returns the number of steps it takes to reduce it to 1"""
    steps = 0

    while num > 1:
        steps = steps + 1
        if num % 2 == 1:
            num = int(num * 3 + 1)
        else:
            num = int(num / 2)

    return steps

print(hailstone_steps(3))
