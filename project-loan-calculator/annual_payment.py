import math


def annual_payment():
    print("Enter the loan principal:")
    p = float(input())

    print("Enter the number of periods:")
    n = float(input())

    print("Enter the loan interest:")
    loan_interest = float(input())
    loan_interest /= 100

    i = loan_interest / 12

    annuity_payment = p * (
        (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
    )

    return print(f"Your monthly payment = {annuity_payment}!")
