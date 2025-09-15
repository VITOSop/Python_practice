
l1=[10,20,30,40,50,60]

print(l1[0])
print(l1[len(l1)-1]) #l1[5]
print(l1)
#----insert

l1.insert(2,100)
print("Inserting....")
print(l1)

#----update

l1[4]=99999
print("Updating.....")
print(l1)

#----remove

l1.remove(60)
print("REmoving....")
print(l1)
