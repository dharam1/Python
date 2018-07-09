#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#everse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    n = int(input())
    operation = []
    for _ in range(1,n+1):
        inp = input()
        values = inp.split()
        if(values[0] == "insert"):
            operation.insert(int(values[1]),int(values[2]))
        elif(values[0] == "remove"):
            operation.remove(int(values[1]))
        elif(values[0] == "sort"):
            operation.sort()
        elif(values[0] == "pop"):
            operation.pop()
        elif(values[0] == "reverse"):
            operation.reverse()
        elif(values[0] == "append"):
            operation.append(int(values[1]))
        else:
            print(operation)
            