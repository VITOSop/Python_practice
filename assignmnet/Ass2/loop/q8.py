

terms=int(input("Enter no of terms to be generated: "))

i=0
num=0
sum=0
while i<terms:
    num=(num*10)+9
    print(num)
    sum+=num
    i+=1

print("Sum is:",sum)
