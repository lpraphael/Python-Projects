import math
import argparse
from number_of_months import number_of_months
from annual_payment import annual_payment
from total_amount_calculator import total_amount


parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["diff", "annuity"])

parser.add_argument("--principal")

parser.add_argument("--periods")

parser.add_argument("--interest")

parser.add_argument("--payment")

args = parser.parse_args()


def loan_calculator():

    if not args.type or (args.type != "diff" and args.type != "annuity"):
        return print("Incorrect parameters")

    if args.type == "diff":
        if not args.principal or not args.periods or not args.interest:
            return print("Incorrect parameters")

        total_value = 0

        i = float(args.interest) / (12 * 100)

        n = 1

        for m in range(int(args.periods)):
            diff_payments = (float(args.principal) / int(args.periods)) + (
                i
                * (
                    float(args.principal)
                    - ((float(args.principal) * (n - 1)) / int(args.periods))
                )
            )

            print(f"Month {n}: payment is {math.ceil(diff_payments)}")
            n += 1
            total_value += math.ceil(diff_payments)

        return print(f"Overpayment = {total_value - float(args.principal)}")

    if args.type == "annuity":

        if args.principal and args.payment and args.interest:
            res = "n"
        elif args.principal and args.periods and args.interest:
            res = "a"
        elif args.payment and args.periods and args.interest:
            res = "p"
        else:
            return print("Incorrect parameters")

    if res == "n":
        number_of_months(args.principal, args.payment, args.interest)
    elif res == "a":
        annual_payment(args.principal, args.periods, args.interest)
    elif res == "p":
        total_amount(args.payment, args.periods, args.interest)


loan_calculator()
