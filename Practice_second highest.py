#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    fmax=-102
    smax=-102
    for i in list(arr):
        if(i>fmax):
            smax = fmax
            fmax = i
        if(i>smax and i != fmax ):
            smax =i
    print (smax)
        
        