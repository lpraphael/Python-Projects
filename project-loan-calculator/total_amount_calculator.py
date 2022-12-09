import math


def total_amount(payment, periods, interest):
    # print("Enter the annuity payment:")
    a = float(payment)

    # print("Enter the number of periods:")
    n = int(periods)

    # print("Enter the loan interest:")
    loan_interest = float(interest)
    loan_interest /= 100

    i = loan_interest / 12

    p = a / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))

    loan_principal = math.ceil(p)

    return print(f"Your loan principal = {loan_principal}!")
