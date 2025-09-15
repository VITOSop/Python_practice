

def hello3():
    for i in range(3):
        print("Hello")

def hello_rec(n):
    if n<3:
        print("Hello")
        hello_rec(n+1)
    else:
        return

hello_rec(4)
