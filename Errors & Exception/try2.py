
def div(a,b):
    try:
        c=a/b #--> zero division exception error exception
        print(c)
    except Exception:
        print("There is some exception")
    except ZeroDivisionError:
        print("There is error in division ",a,b)
    except NameError:
        print("There is undefined variable in the function")
#   except:
#       print("There is some exception in function")
div(10,0)
div(10,b)
div(100,5)
