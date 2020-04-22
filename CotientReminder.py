def quotientReminder(n, d):
    # the theorem of of quotient reminder  ---( n = dq+r )--
    flag = 0
    if d > flag:
        n = (d * (n // d) + (findTheReminder(n, d)))
        return n
    else:
        return "Negative input for d"


def findTheReminder(n, d):
    flag = 0
    if d > flag:
        n = n - d * (n // d)
        return n
    else:
        return "Negative input for d"


def main():
    print("Insert a number for X and Y")
    x = int(input())
    y = int(input())

    res1 = quotientReminder(x, y)
    res2 = findTheReminder(x, y)

    print(f"The the result of operation show that the reminder of a number {x} and {y} is : {res2}")

    print(f"The the result {res1} of operation, proves that x|Y using the Quotient-Reminder Theorem ( n =dq + r)! "
          "and (0 =< r < d) ")  # using f format specifier

    # print("The the result of operation proves that x|Y : {}".format(quotientReminder(x, y)))

main()
