#2. Below you'll find a divide function. Write exception handling so that we catch 
# ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.
#divide(a, b)
#   print(a / b)

def divide(a,b):
    try:
        f_a = float(a)
        f_b = float(b)
        print(f_a / f_b)
    except ZeroDivisionError as e_zde:
        raise ZeroDivisionError(f"Oops, you tried to do a zero division, {e_zde}")
    except TypeError as e_te:
        raise TypeError(f"Oops, you send somenthing unespected : {e_te}")
    except ArithmeticError as e_ae:
        raise ArithmeticError(f"Oops, something else is wrong: {e_ae}")


n1 = input("Hi, inform a number to be divided: ")
n2 = input("Now, inform the next one: ")

divide(n1,n2)