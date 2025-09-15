def palindrome(s1):          
    if (s1[::]==s1[::-1] ) :
        return 1           
    else:        
        return 0 

s1="eacbcae"
   
print(palindrome(s1))
