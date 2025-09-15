
def outer():
    ov1=100
    def inner():
        nonlocal ov1
        v1=100
        print("inner::",ov1,v1)
        
        ov1=200
        print("inner::",ov1,v1)
    inner()
    print("outer::",ov1)

g1=999
outer()
