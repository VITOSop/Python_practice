#write decorator in python which will print  5time * before and after call#


import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*arg,**kwarg):
        # Do something before
        print("*"*5)
        value=func(*arg,**kwarg)
        # Do something after
        print("*"*5,value)
        return value
    return wrapper_decorator


################ write function which u will decorate#########

@decorator
def func1():
    print("This is func1")
func1()



