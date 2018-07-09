#   Print the foll pattern of size input by user
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------


if __name__ == '__main__':
    ip = input()
    split = list(map(int,ip.split()))
    r = split[0]
    c= split[1]
    s=".|."
    for i in range(int(r/2)):
        print((s).center(c,"-"))
        s = s + ".|..|."
    s = s[6:]
    #print (s)
    print(("WELCOME").center(c,"-"))
    for i in range(int(r/2),r-1):
        print((s).center(c,"-"))
        s = s[6:]