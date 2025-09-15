

def infinite_seq():
    num=0
    while True:
        yield num
        num+=1
seql=infinite_seq()

for i in range(100):
    print(next(seql))

