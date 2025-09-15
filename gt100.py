#write program to accept 5 no from user and break loop is num is > 100

count=0
while count<5:
	num=int(input("Enter no:"))
        if(num>100):
                print("Breaking from loop....")
                break
	count+=1
print(num)



############################################

for i in range(5):
	num=int(input("Enter no:"))
	if(num>100):
		print("Breaking from loop....")
		break
print(num)
