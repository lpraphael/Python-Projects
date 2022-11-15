from number_of_months import number_of_months
from annual_payment import annual_payment
from total_amount_calculator import total_amount


def loan_calculator():

    print(
        """
    What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:
    """
    )

    res = input()

    if res == 'n':
        number_of_months()
    elif res == 'a':
        annual_payment()
    elif res == 'p':
        total_amount()


loan_calculator()
