
num=int(input("Enter seconds:"))

hr=num//3600
min=(num%3600)//60
sec=(num%3600)%60
print(hr,":",min,":",sec)
