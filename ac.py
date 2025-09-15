"""  take 5 student mark and make grand total only if student is passed add
 his/her marks in grand total only if student is passed , passing criteria 
is >=40"""

gt_total=0
for i in range(5):
	marks=int(input("Enter marks"))
		if marks<=40:
			continue
		else:
			gt_total+=marks
print(gt_total)
