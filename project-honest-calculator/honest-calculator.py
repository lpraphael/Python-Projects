def honest_calculator():
    MSG_0 = "Enter an equation"
    MSG_1 = "Do you even know what numbers are? Stay focused!"
    MSG_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    MSG_3 = "Yeah... division by zero. Smart move..."

    print(MSG_0)
    equation = input()

    x, oper, y = equation.split()

    try:
        x = float(x)
        y = float(y)

        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/':
            if x == 0 or y == 0:
                raise ZeroDivisionError
            result = x * y
            
        else:
            raise SyntaxError

        return print(result)

    except (TypeError, ValueError):
        print(MSG_1)
        honest_calculator()

    except SyntaxError:
        print(MSG_2)
        honest_calculator()
    except ZeroDivisionError:
        print(MSG_3)
        honest_calculator()
        

honest_calculator()
