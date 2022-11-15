import math


def total_amount():
    print("Enter the annuity payment:")
    a = float(input())

    print("Enter the number of periods:")
    n = int(input())

    print("Enter the loan interest:")
    loan_interest = float(input())
    loan_interest /= 100

    i = loan_interest / 12

    p = a / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))

    return print(f"Your loan principal = {p}!")
