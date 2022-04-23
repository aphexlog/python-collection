def bare_except():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")



if __name__ == '__main__':
    bare_except()
