

i=1
sum=0
mul=1
while i>0:
    num=int(input("Enter no:"))
    ch=input("Press q if you want to exit:")
    
    if(ch=='q')|(ch=='Q'):
        break
    else:
        sum=sum+num
        mul=mul*num
        avg=sum/i
    i+=1
print("Average is:",avg)
print("Product is:",mul)
