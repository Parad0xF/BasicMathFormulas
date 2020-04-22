import fractions
import math


def gcd(numberX, numberY):
    return numberX if not numberY else gcd(numberY, numberX % numberY)

def main():
    print("Type a number for x and y to find the GCF")
    x = int(input())
    y = int(input())
    result = gcd(x, y)
    print(f"The GCD of the number {x} and {y} is: {result}")

    work = math.gcd


    print(work(x,y))

main()
