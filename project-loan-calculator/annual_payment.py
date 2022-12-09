import math


def annual_payment(principal, periods, interest):
    # print("Enter the loan principal:")
    p = float(principal)

    # print("Enter the number of periods:")
    n = float(periods)

    # print("Enter the loan interest:")
    loan_interest = float(interest)
    loan_interest /= 100

    i = loan_interest / 12

    annuity_payment = p * (
        (i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)
    )

    monthly_payment = math.ceil(annuity_payment)

    return print(f"Your monthly payment = {monthly_payment}!")
