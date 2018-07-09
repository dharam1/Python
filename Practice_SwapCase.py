#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    res = ""
    for i in s:
        if(ord(i) in range(97,123)):
            res+=chr(ord(i)-32)
            #print(chr(ord(i)-32))
        elif(ord(i) in range(65,91)):
            res+=chr(ord(i)+32)  
            #print(chr(ord(i)+32))
        else:
            res+=i
    return res