#   Print below pattern of size entered by user 
size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------



def print_rangoli(size):
    r = size
    c = r * 3
    ch = chr(97+size-1)
    s = chr(97+size-1)
    rev = ""
    backup = ""
    for i in range(int(r)):
        print((s).rjust(int(c/2)+2,"-"),(rev).ljust(int(c/2)+1,"-"),sep="")
        s = s + "-" +chr(ord(ch)-1)
        ch = chr(ord(ch)-1)
        #print((rev).ljust(int(c/2)+1,"-"))
        backup = s[:len(s)-1]
        rev = backup[::-1]
    
    s = s[:len(s)-2]
    backup = s[:len(s)-1]
    rev = backup[::-1]
    for i in range (int(r)-1):
        s = s[:len(s)-2]
        backup = s[:len(s)-1]
        rev = backup[::-1]
        print((s).rjust(int(c/2)+2,"-"),(rev).ljust(int(c/2)+1,"-"),sep="")
        
        
    