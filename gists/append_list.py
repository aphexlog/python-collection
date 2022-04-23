# wrong
def apend(n, l=[]):
    l.append(n)
    return l

if __name__ == '__main__':
    print(apend(1))
    print(apend(2))
    print(apend(3))

# correct
def append(n, l=None):
    if l is None:
        l = []
    l.append(n)
    return l

if __name__ == '__main__':
    print(append(1))
    print(append(2))
    print(append(3))
