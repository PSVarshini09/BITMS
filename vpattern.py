n=str(input('enter name'))
length=len(n)
for i in range(length):
    for j in range(length*2):
        if i==j or j==length*2-1-i:
            print(n[i],end=' ')
        else:
            print(' ',end=' ')
    print()