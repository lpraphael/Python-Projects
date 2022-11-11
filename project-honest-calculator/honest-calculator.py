def honest_calculator():
    MSG_0 = "Enter an equation"
    MSG_1 = "Do you even know what numbers are? Stay focused!"
    MSG_2 = '''Yes, an interesting math operation.
            You've slept through all classes, haven't you?'''
    MSG_3 = "Yeah, division by zero. Smart move..."
    MSG_4 = "Do you want to store the result? (y / n):"
    MSG_5 = "Do you want to continue calculations? (y / n):"
    memory = 0
    result = "y"

    while result == "y":

        print(MSG_0)
        equation = input()

        x, oper, y = equation.split()

        if x == "M":
            x = memory

        if y == "M":
            y = memory

        try:
            x = float(x)
            y = float(y)

            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/":
                if x == 0 or y == 0:
                    raise ZeroDivisionError
                result = x * y

            else:
                raise SyntaxError

            print(result)

            print(MSG_4)

            answer_1 = input()

            if answer_1 == "y":
                memory = result

            print(MSG_5)

            answer_2 = input()

            result = answer_2

        except (TypeError, ValueError):
            print(MSG_1)
            result = "y"
        except SyntaxError:
            print(MSG_2)
            result = "y"
        except ZeroDivisionError:
            print(MSG_3)
            result = "y"

    return None


honest_calculator()
