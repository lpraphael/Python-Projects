import math


def number_of_months():
    print("Enter the loan principal:")
    loan_principal = float(input())

    print("Enter the monthly payment:")
    monthly_payment = float(input())

    print("Enter the loan interest:")
    loan_interest = float(input())
    loan_interest /= 100

    i = loan_interest / 12

    calc = monthly_payment / (monthly_payment - (i * loan_principal))

    n = math.log(calc, (1 + i))

    years = int(math.ceil(n) / 12)

    months = int(math.ceil(n) % 12)

    return print(
        f"It will take {years} years and {months} months to repay this loan!"
    )
