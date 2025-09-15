
s1=input("Enter string:")

s1=s1.split(" ")

result = s1[0]
for ch in s1:
    if(len(ch)>len(result)):
        result = ch
        print(result)
        

print(len(result))

