
p1="aa bb aa cc bb cc aa"
l1=p1.split(" ")
word_coun={}

for e1 in l1:
    if e1 in word_count: 
        word_count[e1]+=1
    else:
        word_count[e1]=1
print(word_count)
