f = open('file.txt', 'a+')#w -> Overwrite file ; r -> Read a file ; a -> append a file
try:
    #f.write("append Done!!!")
    line_count = 0
    for i in f:
        #line_count += 1
        print(i)
    #print("Lines Count",line_count)
    print(f.read()) 
finally:
    f.close()