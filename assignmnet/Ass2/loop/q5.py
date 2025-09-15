
num=int(input("Enter no:"))

count=0
while num>0:
    digit=num%10
    num=num//10
    print(digit)
    count+=1
print("Total digit: ",count)


