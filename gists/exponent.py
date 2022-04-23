def exponent(x = None):
    """
    Outputs the exponent of x.
    """
    while True:
        try:
            x = int(input("Please enter a number: "))
            result = x ** 2
            print(result)
            break
        except TypeError:
            print("Oops!  That was not a valid number.  Try again...")


if __name__ == '__main__':
    exponent()