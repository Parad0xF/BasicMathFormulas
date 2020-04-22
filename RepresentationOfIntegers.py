def findTheReminder(n, d):
    flag = 0
    if d > flag:
        n = n - d * (n // d)
        return n
    else:
        return "Negative input for d"


def representationOfInt(n):
    divider = 2
    if findTheReminder(n, divider):
        q = (n - findTheReminder(n, divider)) / 2
        n = divider * q + findTheReminder(n, divider)
        print(f"The number {n} is odd by the Theorem ( n = 2q + 1)")
    else:
        q = (n - findTheReminder(n, divider)) / 2
        n = divider * q + findTheReminder(n, divider)
        print(f"The number {n} is even by the Theorem ( n = 2q + 0)")


def main():
    print("Check whether the number X is even or odd ")
    x = int(input())

    representationOfInt(x)


main()
