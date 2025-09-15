
num=int(input("Enter no:"))

if num==2:
    print("Prime no.")

i=2
while i<(num/2):
    if num%i==0:
        print("Not prime.")
        break
    i+=1
else:
    print("Prime no.")
