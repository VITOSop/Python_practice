#!/usr/bin/python3

marks=int(input("Enter marks:"))

if  marks < 25:
	print("F")
elif marks < 45:     #25 <= marks <45
	print("E")
elif marks < 50:     #45 <= marks <50
	print("D")
elif marks < 60:
        print("C")    
elif marks < 80:
        print("B")     
else:
        print("A")

