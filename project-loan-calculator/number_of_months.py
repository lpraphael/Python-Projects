import math


def number_of_months(principal, payment, interest):
    # print("Enter the loan principal:")
    loan_principal = float(principal)

    # print("Enter the monthly payment:")
    monthly_payment = float(payment)

    # print("Enter the loan interest:")
    loan_interest = float(interest)
    loan_interest /= 100

    i = loan_interest / 12

    calc = monthly_payment / (monthly_payment - (i * loan_principal))

    n = math.log(calc, (1 + i))

    years = int(math.ceil(n) / 12)

    months = int(math.ceil(n) % 12)

    if months == 0:
        return print(
            f"It will take {years} years to repay this loan!"
            f"Overpayment = {(monthly_payment * (years * 12))-loan_principal}"
        )

    return print(
        f"It will take {years} years and {months} months to repay this loan!"
    )
