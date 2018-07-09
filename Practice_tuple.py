#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
if __name__ == '__main__':
    n = int(input())
    integer_list = list((map(int, input().split())))
    tup = ()
    for i in integer_list:
        tup = tup + (i,)
    print (hash(tup))
    
    #integer_list = tuple((map(int, input().split())))  --- Direct tupple conversion
    
        
        
        