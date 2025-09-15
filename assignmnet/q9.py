
while 1:
    ch=input("Enter---1.Binary\t2.Octal\t3.Hex\t4.Exit")
    s1=input("Give string to be converted to:")

    if(ch==1):
        n=int(s1,base=2)
        print("bin=",s1,"int=",n)
    elif(ch==2):
        n=int(s1,base=8)
        print("oct=",s1,"int=",n)
    elif(ch==3):
        n=int(s1,base=16)
        print("oct=",s1,"int=",n)
    else:
        print("Exiting")
