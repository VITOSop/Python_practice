#!/usr/bin/python3

unit=int(input("Enter no of unit:"))
bill=0
if(unit<=100):
	print("Light bill is",bill)
elif(100<unit<=200):
	bill=(unit-100)*5
	print("Light bill is",bill)
elif(unit>200):
	bill=(100*5)+(unit-200)*10
	print("Light bill is",bill)
else:
	print("Enter correct no of unit:")


####################################################

unit=int(input("Enter no of unit:"))
bill=0
if units > 200:
	bill=(units-200)*10
	bill=200
if units > 100:
	bill=(units-100)*5
