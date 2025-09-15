"""write program to input from user till time user give q input , when user 
give q  break loop
"""

#NOTE : when we dont have fix no of iteration , we prefer while loop

while 1: #infinite while loop
	ch=input("Enter input:")
	if (ch=='q') | (ch=='Q'):
		print("Breaking 1st loop...")
		break
##############################################################

print("Starting 2nd loop:")
ch=''
while (ch!='q') & (ch!='Q'):
	ch=input("Enter input:")
	print("You entered ",ch)	

