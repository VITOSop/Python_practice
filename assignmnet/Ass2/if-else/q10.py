price=int(input("Enter price of bike:"))
tax=0
inssurance=0
if(price>100000):
	tax=(price*0.15)
	inssurance=(price*0.20)
	amount=price+tax+inssurance
	print("Total amount to be paid is ",amount)
elif(50000<price<=100000):
	tax=(price*0.10)
	inssurance=(price*0.08)
	amount=price+tax+inssurance
	print("Total amount to be paid is ",amount)
elif(price<=50000):
	tax=(price*0.05)
	inssurance=(price*0.05)
	amount=price+tax+inssurance
	print("Total amount to be paid is ",amount)
else:
	print("Enter corret price:")
