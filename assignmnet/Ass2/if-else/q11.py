
amount=int(input("Enter amount:"))
no1=0
no2=0
no5=0
no10=0
no50=0
no100=0
no500=0
no2000=0
if  amount>=2000:
	no2000=(amount//2000)
	amount=amount-2000*no2000
if amount>=500:
	no500=(amount//500)
	amount=amount-500*no500
if amount>=100:
	no100=(amount//100)
	amount=amount-100
if amount>=50:
        no50=(amount//50)
        amount=amount-50
if amount>=10:
        no10=(amount//10)
        amount=amount-10
if amount>=5:
	no5=(amount//5)
	amount=amount-5
if amount>=2:
	no2=(amount//2)
	amount=amount-2
else:
	no1=1
print(no1,no2,no5,no10,no50,no100,no500,no2000)

#################################################

notes=[2000,500,100,50,10,5,2,1]
amount=int(input("Enter amount given :"))
for note in notes:
	num=amount//note
	print(note,":",num)
	amount=amount%note
