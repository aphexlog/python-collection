# decorator function
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('before')
        func(*args, **kwargs)
        print('after')
    return wrap_func
