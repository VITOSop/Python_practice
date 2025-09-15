
while 1:
    ch=input("Enter---1.Binary\t2.Octal\t3.Hex\t4.Exit")
    s1=input("Give string to be converted to:")
    match ch:
    case '1':
        n=int(s1,base=2)
        print("bin=",s1,"int=",n)
    case '2':
        n=int(s1,base=8)
        print("oct=",s1,"int=",n)
    case '3':
        n=int(s1,base=16)
        print("hex=",s1,"int=",n)
    case '4:'
        print("Exiting")
        break





