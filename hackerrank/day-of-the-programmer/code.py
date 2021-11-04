#!/bin/python3

import math
import os
import random
import re
import sys

#
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    # if it is 1918 then the day is 26 sept
    if year == 1918:
        return f"26.09.{year}"
    # if its in julian cal then divisible by 4 is enough for leap year
    if year <= 1917 and year % 4 == 0:
        return f"12.09.{year}"
    # if its in Gregorian calendar then leap year condition
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
