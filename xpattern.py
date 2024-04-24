text=input('enter text')
length=len(text)
for i in range(length):
    for j in range(length):
        if(i==j) or ((i+j)==length-1):
            print("{0}".format(text[i]),end=' ')
        else:
            print(" ",end=' ')
    print()