

def string_1(s1):
    l1=s1.split(" ")
    for e1 in l1:        
        if e1.count("s")==2:
            print(e1)          


s=input("Enter string:")
string_1(s)
