#wap to take 5 no from user if no is less <40  bfreak loop if all no gt 40
# print total

i=0
total=0
while i<5:
	marks=int(input("Enter no:"))
	if marks<40:
		break
	total=total+marks
	i+=1
else:
	#executed when in while loop break is not executed
	print(total)
