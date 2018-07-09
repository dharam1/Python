# Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .


def merge_the_tools(string, k):
    divide =int(len(string)/k)
    divide_len = len(string)//divide
    substr = []
    i = 0
    while(i < len(string)):
        #print(i)
        sub = string[i:divide_len+i]
        i = i + divide_len
        substr.append(sub)
    #print(substr)
    occur = []
    #print(len(substr))
    for i in substr:
        occur.clear()
        res =""
        for j in i:
            if (j not in occur):
                occur.append(j)
                res = res + j
        print (res)
        
            
        
        