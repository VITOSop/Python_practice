num=int(input("Enter no:"))
			
i=2
while i<num/2:
	if(num%i==0):
		print(num,"is not prime!!!")
		break
	i+=1
else:
	print("No is prime no!!!") 

#####################################################
#Efficent programe 1

num=int(input("Enter no:"))

if num%2==0:
    print("Prime no")
else
	i=3
	while i<(num//2):
		if num%i==0:
			print("Not prime")
			break
	i=i+2
	else:	
		print("Prime no")

##########################################################
#Efficient program 2
num=int(input("Enter no:"))

if num%2==0:
        print("Prime no")
if num%2==0:
        print("Prime no")
else
        i=3
        while i<int(num**0.5):  #int(pow(num,0.5))  #import math int(math.sqrt(num))
                if num%i==0:
                        print("Not prime")
                        break
        i=i+2
        else:   
                print("Prime no")

