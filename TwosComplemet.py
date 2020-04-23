# Radu Enachi
# 22 Apr 2020 is a Wednesday on the 22 day of April.
from datetime import datetime
import numpy


def convertDecimal(number):
    lis = []
    while number > 1:
        number = number // 2
        if number % 2 == 0:
            lis.append(0)
        else:
            lis.append(1)
    lis.reverse()
    return lis


def rightShift(seq):
    return [seq[-1]] + seq[:-1]


def twosComplement(a):
    q = [x + 1 if x == 0 else x - 1 for x in a]
    if q[-1] == 0:
        q.pop(-1)
        q.append(1)
    else:
        q = numpy.roll(q, -1)  # shift to the left
        q[-1] = 1
    return q


def main():
    temp_list = []
    user_input = int(input("Enter the number:   "))
    theList = convertDecimal(user_input)
    print("Initial binary format: ", *theList, sep='')
    print(f"Tow's complement of the value:", *twosComplement(theList), sep=' ')

    now = datetime.today()
    print(now.strftime(" %d %b %Y is a %A on the %d day of %B."))


main()
