
def palindrome(s): 
    if (s[::]==s[::-1]):
        return True
    else:
        return False


s1="123abccba321"
print(palindrome(s1))
