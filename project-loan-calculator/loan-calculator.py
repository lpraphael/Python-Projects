import math


def loan_calculator():

    loan_principal = int(input("Enter the loan principal:\n"))

    print(
        """
    What do you want to calculate?
    type "m" for number of monthly payments,
    type "p" for the monthly payment:
    """
    )

    response = input()

    if response == "m":
        print("Enter the monthly payment:")
        monthly_payment = float(input())

        result = math.ceil(loan_principal / monthly_payment)

        if result == 1:
            return print("It will take", result, "month to repay the loan")

        return print("It will take", result, "months to repay the loan")

    elif response == "p":
        print("Enter the number of months:")
        number_of_months = int(input())

        payment = math.ceil(loan_principal / number_of_months)

        last_payment = loan_principal - ((number_of_months - 1) * payment)

        return print(
            "Your monthly payment = ",
            payment,
            "and the last payment = ",
            last_payment,
            ".",
        )


loan_calculator()
