
import functools

def bold_decorator(func):
    def wrapper():
        return f"<b>{func()}<b>"
    return wrapper

def italic_decorator(func):
    def wrapper():
        return f"<i>{func()}<i>"
    return wrapper

def underline_decorator(func):
    def wrapper():
        return f"<u>{func()}<u>"
    return wrapper

def number():
    return 10

@bold_decorator
def bold_number():
    return number()

@italic_decorator
def italic_number():
    return number()

@underline_decorator
def underline_number():
    return number()



print("Bold::",bold_number())
print("Italic::",italic_number())
print("Underline::",underline_number())

