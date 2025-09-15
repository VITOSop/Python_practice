
import string
def pangram(s):
    s=s.lower()
    l1=list(s.replace(" ",""))

    l2=list(string.ascii_lowercase)
#l2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if len(l1)<26:
        print("Not pangram.")
    else:
        for e1 in l2:
            if e1 not in l1:
                print("Not pangram")
                break;
        else:
            print("Pangram")


s="The quick brown fox jumps over the lazy dog"
pangram(s)
