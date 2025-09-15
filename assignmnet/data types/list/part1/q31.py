
l1=[10,20,30,40,50,60,70,80,90]

str=int(input("Enter start:"))
end=int(input("Enter end:"))

list=l1[str:end]

count=len(list)

print("Original list=",l1)
print(f"slice from index {str} to {end-1}:",list)
print("No os elements in slice:",count)
