"""Calculate delivery charges for online ketring company,
	1st  5km 	charges are  0
	6 to 10km	charges are  10
	 > 10		charges are  20

"""

distance=int(input("Enter distance:"))

amount=0
if distance>10:
	amount=(distance-10)*20
	distance=10
if distance>5:
	amount=amount+(distance-5)*10
else:
	amount=0
print(amount)
