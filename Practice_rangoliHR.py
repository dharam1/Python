
def print_rangoli(size):
    r = size
    c = r * 3
    ch = chr(97+size-1)
    s = chr(97+size-1)
    rev = ""
    backup = ""
    for i in range(int(r)):
        print((s).rjust(int(c/2)+2,"-"),(rev).ljust(int(c/2)+1,"-"))
        s = s + "-" +chr(ord(ch)-1)
        ch = chr(ord(ch)-1)
        #print((rev).ljust(int(c/2)+1,"-"))
        backup = s[:len(s)-1]
        rev = backup[::-1]
    s = s[:len(s)-2]
    for i in range (int(r)-1):
        s = s[:len(s)-2]
        print((s).rjust(int(c/2)+2,"-"))
        
    