# comprehentions make your code shorter and more readable
def never_using_comprehensions():
    squares = {}
    for i in range(10):
        squares[i] = i * i
    return squares

def using_comprehensions():
    squares = {i: i * i for i in range(10)}
    dict_comp = {i: i * i for i in range(10)}
    list_comp = [i * i for i in range(10)]
    set_comp = {i * i for i in range(10)}
    return squares, dict_comp, list_comp, set_comp

if __name__ == '__main__':
    print(using_comprehensions())
